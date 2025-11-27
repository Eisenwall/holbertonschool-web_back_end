#!/usr/bin/env python3
"""
Function make_multiplier: returns a function that multiplies a float
by the given multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies its argument by multiplier."""
    
    def nb(n: float) -> float:
        return n * multiplier

    return nb
