#!/usr/bin/env python3
""" multiple coroutines at the same time with async """
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ spawns wait random lists n times """
    wait_n_list = [wait_random(max_delay) for _ in range(n)]
    return [await result for result in asyncio.as_completed(wait_n_list)]
