#!/usr/bin/env python3
"""Async Comprehension"""

from typing import List

Vector = List[float]

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Vector:
    """Function that returns a list of 10 random numbers using async comprehension."""
    numbers = [
        value
        async for value in async_generator()
    ]
    return numbers
