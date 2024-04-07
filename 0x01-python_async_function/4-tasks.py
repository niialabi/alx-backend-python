#!/usr/bin/env python3
""" multiple coroutines at the same time with async """
from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ spawns wait random lists n times """
    wait_n_list = [task_wait_random(max_delay) for _ in range(n)]
    return [await result for result in asyncio.as_completed(wait_n_list)]
