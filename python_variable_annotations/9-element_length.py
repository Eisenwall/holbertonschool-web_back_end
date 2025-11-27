#!/usr/bin/env python3
"""
Function element_length: returns a list of tuples with each element of lst
and its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples (element, length of element) from lst."""
    return [(i, len(i)) for i in lst]
