#!/usr/bin/env python3
"""
Function sum_mixed_list: returns the sum of a list containing integers and floats.
"""

from typing import List, Union

# def inp(a: List[Union[float, int]]) -> float:
#     return sum(a)

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of all elements in mxd_lst as a float."""
    return sum(mxd_lst)

