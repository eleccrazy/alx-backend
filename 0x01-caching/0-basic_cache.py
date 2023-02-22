#!/usr/bin/env python3
"""
File: 0-basic_cache.py
Desc: This python module contains code for implementing caching
      system in python.
Author: Gizachew Bayness
Date Created: Feb 22, 2023
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic dictionary"""

    def put(self, key, item):
        """Puts item in cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Gets item from cache"""
        return self.cache_data.get(key, None)
