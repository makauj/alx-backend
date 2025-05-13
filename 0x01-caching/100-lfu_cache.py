#!/usr/bin/env python3
"""LFU cache module"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU Cache class that inherits from BaseCaching"""
    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.cache_data = {}
        self.usage_count = {}

    def put(self, key, item):
        """Add an item to the cache"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_key = min(self.usage_count,
                              key=lambda k: self.usage_count[k])
                del self.cache_data[lfu_key]
                del self.usage_count[lfu_key]
                print("DISCARD: {}".format(lfu_key))
            self.cache_data[key] = item
            self.usage_count[key] = 1

    def get(self, key):
        """Get an item from the cache"""
        if key in self.cache_data:
            self.usage_count[key] += 1
            return self.cache_data[key]
        return None
