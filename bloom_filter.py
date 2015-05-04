# -*- coding: utf-8 -*-
"""
    bloom_filter
    ~~~~~~~~~~~~
    Simple bloom filter in python

    Copyright (C) 2015 Eric Scrivner.
"""
import functools

import mmh3
import bitstring


def get_hash_functions(num_hash_functions):
    """Returns a list containing the given number of different hash functions.

    :param num_hash_functions: The number of hash functions
    :type num_hash_functions: int
    :rtype: list
    """
    results = []
    for i in range(num_hash_functions):
        results.append(functools.partial(mmh3.hash, seed=i))
    return results


class BloomFilter(object):
    """Simple bloom filter interface"""

    def __init__(self, num_hash_functions, bit_vector_length):
        """Create a new bloom filter.

        :param num_hash_functions: The number of unique hash functions
        :type num_hash_functions: int
        :param bit_vector_length: The length of the bit vector
        :type bit_vector_length: int
        """
        self.hash_functions = get_hash_functions(num_hash_functions)
        self.bit_vector = bitstring.BitArray(length=bit_vector_length)

    def _get_bit_position(self, hash_function, item):
        """Returns the bit position of the given item for the given hash
        function.

        :param hash_function: A hash function
        :type hash_function: func
        :param item: An item
        :type item: str or unicode
        """
        return hash_function(item) % len(self.bit_vector)

    def insert(self, item):
        """Inserts the given value into the bloom filter.

        :param item: A string value
        :type item: str or unicode
        """
        for each in self.hash_functions:
            self.bit_vector.set(True, self._get_bit_position(each, item))

    def __contains__(self, item):
        """Indicates whether or not the given item is contained in this bloom
        filter.

        :param item: The item to be checked
        :type item: str or unicode
        """
        required_positions = [
            self._get_bit_position(each, item) for each in self.hash_functions]
        return self.bit_vector.all(True, required_positions)
