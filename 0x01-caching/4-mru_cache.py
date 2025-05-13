#!/usr/bin/env python3
"""MRU Cache Implementation"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU Cache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.cache = {}
        self.most_recently_used = []

    def put(self, key, item):
        """Add an item to the cache"""
        if key and item:
            if len(self.cache) >= BaseCaching.MAX_ITEMS:
                mru_key = self.most_recently_used.pop()
                del self.cache[mru_key]
                print("DISCARD: {}".format(mru_key))
            self.cache[key] = item
            self.most_recently_used.append(key)

    def get(self, key):
        """Get an item from the cache"""
        if key in self.cache:
            self.most_recently_used.remove(key)
            self.most_recently_used.append(key)
            return self.cache[key]
        return None
