#!/usr/bin/env python3
"""
Simple helper function for pagination
"""


from typing import Tuple


def index_range(y: int, p: int) -> Tuple[int, int]:
    """
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for a
    particular page and page_size.

    Args:
        page (int): The current page number (1-indexed)
        page_size (int): The number of items per page

    Returns:
        Tuple[int, int]: A tuple (start_index, end_index)
    """
    s = (y - 1) * p
    e = y * p
    return (s, e)
