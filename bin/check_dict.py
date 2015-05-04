# -*- coding: utf-8 -*-
"""
    check_dict
    ~~~~~~~~~~
    Simple tool to check if the given word is in a dictionary.

    Copyright (C) 2015 Eric Scrivner
"""
import argparse
import math
import sys
sys.path.append('')

import bloom_filter


def probability_of_false_positive(num_hash_funcs, num_items, bit_vec_length):
    """Compute the probability of receiving a false positive for the given
    params.

    :param num_hash_funcs: The number of hash functions
    :type num_hash_funcs: float
    :param num_items: The number of items inserted into the bit vector
    :type num_items: float
    :param bit_vec_length: The length of the bit vector
    :type bit_vec_length: float
    """
    probability_of_success = math.e**(
        (-num_hash_funcs * float(num_items)) / bit_vec_length)
    return (1.0 - probability_of_success)**num_hash_funcs


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Bloom filter based spell checker.')
    parser.add_argument('-k', dest='num_hash_funcs', type=int, default=5,
                        help='Number of hash functions for bloom filter')
    parser.add_argument('-m', dest='bit_vector_length', type=int,
                        default=1024000,
                        help='Number of bits for bloom filter bit vector.')
    args = parser.parse_args()

    false_positive_prob = probability_of_false_positive(
        args.num_hash_funcs, 100000, args.bit_vector_length)
    print 'k', args.num_hash_funcs
    print 'm', args.bit_vector_length
    print 'False positive probability', false_positive_prob

    bloomfilter = bloom_filter.BloomFilter(
        args.num_hash_funcs, args.bit_vector_length)

    sys.stdout.write('Loading dictionary...')
    sys.stdout.flush()
    with open('/usr/share/dict/words', 'r') as dictfile:
        for word in dictfile:
            bloomfilter.insert(word.strip())
    print 'DONE!'
    print

    print 'Enter a word to check for membership in the dictionary followed'
    print 'by ENTER.'
    print
    print 'Enter :q followed by ENTER to quit.'
    print
    while True:
        word = raw_input('Word to check: ')
        if word == ':q':
            break
        print (word.lower() in bloomfilter)
