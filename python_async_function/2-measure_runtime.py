#!/usr/bin/env python3
"""Module 2-measure_runtime
Measures the average runtime of the wait_n coroutine.
"""

import asyncio
import time
from typing import Any

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time for wait_n(n, max_delay)
    and return the average time per coroutine.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
