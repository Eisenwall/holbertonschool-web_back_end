#!/usr/bin/env python3
"""Hypermedia pagination module."""

import csv
import math
from typing import List, Dict
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize server with no cached dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset from the CSV file.

        Returns:
            List[List]: list of rows excluding header
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, newline='') as f:
                reader = csv.reader(f)
                all_rows = [row for row in reader]
            self.__dataset = all_rows[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of the dataset.

        Args:
            page (int): page number (1-indexed)
            page_size (int): number of items per page

        Returns:
            List[List]: list of rows corresponding to the requested page
        """
        assert isinstance(page, int) and page > 0, "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"

        start_idx, end_idx = index_range(page, page_size)
        data = self.dataset()

        if start_idx >= len(data):
            return []

        return data[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Return a dictionary containing hypermedia pagination information.

        Args:
            page (int): current page number (1-indexed)
            page_size (int): number of items per page

        Returns:
            Dict: dictionary with keys page_size, page, data, next_page,
                  prev_page, total_pages
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        hyper_dict = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

        return hyper_dict
