#!/usr/bin/env python3
""" measure runtime module """

from time import perf_counter
from asyncio import gather

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """ func to measure runtime """
    start_time = perf_counter()
    await gather(*(async_comprehension() for _ in range(4)))
    return perf_counter() - start_time
