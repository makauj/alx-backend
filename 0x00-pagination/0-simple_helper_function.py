#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page: int, page_size: int) -> tuple:
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
