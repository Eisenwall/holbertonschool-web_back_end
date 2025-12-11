#!/usr/bin/env python3
"""Module for simple pagination of baby names dataset."""

import csv
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to provide paginated access to the baby names dataset."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server with an empty dataset cache."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset from CSV if not already loaded.

        Returns:
            List[List]: The dataset as a list of rows (excluding header)
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, newline='') as f:
                reader = csv.reader(f)
                all_rows = [row for row in reader]
            self.__dataset = all_rows[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of data from the dataset.

        Args:
            page (int, optional): Page number starting from 1. Defaults to 1.
            page_size (int, optional): Number of items per page. Defaults to 10.

        Returns:
            List[List]: List of rows corresponding to the requested page
        """
        assert isinstance(page, int) and page > 0, "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"

        start_idx, end_idx = index_range(page, page_size)
        data = self.dataset()
        if start_idx >= len(data):
            return []

        return data[start_idx:end_idx]
