#!/usr/bin/env python3
''' Async Comprehension '''
from typing import List
l = List[float]

foc = __import__('0-async_generator').async_generator


async def async_comprehension() -> l:
    ''' Function that return a list '''
    d = [s async for s in foc()]
    return d
