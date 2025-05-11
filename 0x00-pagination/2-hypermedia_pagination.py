#!/usr/bin/env python3
"""simple pagination"""


from typing import List, Tuple, Dict
import csv
from math import ceil


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function that calculates the start and end index to paginate a dataset.

    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.
    Returns:
        tuple: A tuple containing the start and end index for the page.
    """
    if page <= 0 or page_size <= 0:
        return (0, 0)
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        get_page method:
        - page: integer page number
        - page_size: number of items per page
        - return: list of items on the page
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index > len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int, page_size: int) -> Dict:
        """
        get_hyper method:
        - page: integer page number
        - page_size: number of items per page
        - return: dictionary with pagination information
        """
        dataset = self.dataset()
        total_items = len(dataset)
        start_index, end_index = index_range(page, page_size)
        if page_size <= 0 or page <= 0:
            return {
                'page_size': 0,
                'page': page,
                'data': [],
                'next_page': None,
                'prev_page': None,
                'total_pages': 0
            }

        if start_index >= total_items:
            return {
                'page_size': 0,
                'page': page,
                'data': [],
                'next_page': None,
                'prev_page': None,
                'total_pages': 0
            }

        data = dataset[start_index:end_index]
        next_page = page + 1 if end_index < total_items else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': (total_items + page_size - 1) // page_size
        }
