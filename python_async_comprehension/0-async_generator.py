#!/usr/bin/env python3
"""Generator that yields 10 random numbers with a 1-second delay"""

import random
import time
from typing import Generator


def async_generator() -> Generator[float, None, None]:
    """Generator that yields a random number between 0 and 10
    every second for 10 iterations.
    """
    for _ in range(10):
        time.sleep(1)
        yield random.uniform(0, 10)
