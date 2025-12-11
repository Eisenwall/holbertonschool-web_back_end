#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize dataset caches."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Load and cache dataset from CSV (excluding header)."""
        if self.__dataset is None:
            with open(self.DATA_FILE, newline='') as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return dataset indexed by position for deletion-resilient pagination."""
        if self.__indexed_dataset is None:
            data = self.dataset()
            self.__indexed_dataset = {i: data[i] for i in range(len(data))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """
        Return a page starting at `index`, resilient to deleted entries.

        Args:
            index (int): starting index of the page
            page_size (int): number of items in the page

        Returns:
            Dict: dictionary with keys: index, next_index, page_size, data
        """
        assert isinstance(index, int) and isinstance(page_size, int), "index and page_size must be integers"
        assert 0 <= index < len(self.dataset()), "index out of range"

        data_page = []
        next_idx = index
        indexed_data = self.indexed_dataset()

        for _ in range(page_size):
            while next_idx not in indexed_data and next_idx < len(indexed_data):
                next_idx += 1
            if next_idx < len(indexed_data):
                data_page.append(indexed_data[next_idx])
                next_idx += 1

        return {
            "index": index,
            "next_index": next_idx,
            "page_size": len(data_page),
            "data": data_page
        }
