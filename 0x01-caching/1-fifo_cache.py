#!/usr/bin/env python3
"""FIFO cache module"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize the FIFO cache"""
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """Add an item to the cache using FIFO policy"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the first item added (FIFO)
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print("DISCARD:", first_key)
            self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
