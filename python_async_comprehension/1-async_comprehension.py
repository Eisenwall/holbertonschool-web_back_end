#!/usr/bin/env python3
"""Async comprehension collecting numbers from async_generator"""

from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using an async comprehension over async_generator."""
    return [i async for i in async_generator()]
