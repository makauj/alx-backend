#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Tuple, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Function retrieves information from a given index

        Args:
            index (int, optional):Defaults to None.
            page_size (int, optional): Defaults to 10.

        Returns:
            Dict: A dictionary containing the page data, next index,
            and total number of pages.
        """
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.indexed_dataset()
        total_data = len(dataset)
        total_pages = math.ceil(total_data / page_size)

        if index >= total_data:
            return {
                "page_size": 0,
                "data": [],
                "next_index": None,
                "total_pages": total_pages
            }

        next_index = index + page_size
        data = [dataset[i] for i in range(index, min(next_index, total_data))]

        return {
            "page_size": len(data),
            "data": data,
            "next_index": next_index if next_index < total_data else None,
            "total_pages": total_pages
        }
