#!/usr/bin/env python3
"""
Function to_kv: returns a tuple where the first element is a string k
and the second element is the square of v as a float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple (k, v squared as float)."""
    return (k, float(v ** 2))
