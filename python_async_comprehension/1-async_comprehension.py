#!/usr/bin/env python3
"""Async comprehension collecting numbers from async_generator"""

from typing import List

Vector = List[float]

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Vector:
    """Collect 10 random numbers using async comprehension from async_generator."""
    numbers: Vector = [
        number
        async for number in async_generator()
    ]
    return numbers
