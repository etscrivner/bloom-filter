# bloom-filter
A simple python bloom filter using murmur3 hashes.

# Usage

```python
import bloom_filter

bf = bloom_filter.BloomFilter(num_hash_functions=5, bit_vector_length=1024000)
bf.insert('Hello')
assert 'Hello' in bf
```

# Command-Line Spell Checker

There's also a simple spell-checker that you can use to check various words for their membership in the system dictionary.

```shell
$ python bin/check_dict.py
To git@github.com:etscrivner/bloom-filter.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
(kata6)eric@eric-VirtualBox:~/Code/python/bloom_filter$ python bin/check_dict.py
k 5
m 1024000
False positive probability 0.00860467655328
Loading dictionary...DONE!

Enter a word to check for membership in the dictionary followed
by ENTER.

Enter :q followed by ENTER to quit.

Word to check: Hello
True
Word to check: :q
```
