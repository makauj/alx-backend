#!/usr/bin/env python3
"""LIFO cache module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.cache_data = {}
        self.last_key = None

    def put(self, key, item):
        """Add an item to the cache"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.last_key:
                    del self.cache_data[self.last_key]
                    print("DISCARD: {}".format(self.last_key))
            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """Get an item from the cache"""
        return self.cache_data.get(key, None)
