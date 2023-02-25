#!/usr/bin/env python3
"""
File: 2-lifo_cache.py
Desc: This python module contains code for implementing caching
      system in python.
Author: Gizachew Bayness
Date Created: Feb 22, 2023
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Cache"""
    st = []

    def __init__(self):
        '''Intialization'''
        super().__init__()

    def put(self, key, item):
        """Stores a new key value pairt to the cache"""
        if (key is not None and item is not None):
            self.cache_data[key] = item
            self.st.append(key)

        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            key_to_be_removed = LIFOCache.st[-2]
            self.cache_data.pop(key_to_be_removed)
            print('DISCARD: {}'.format(LIFOCache.st.pop(-2)))

    def get(self, key):
        """Returns the item based on the key"""
        if (key is None or key not in self.cache_data.keys()):
            return None
        return self.cache_data[key]
