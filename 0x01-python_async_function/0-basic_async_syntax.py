#!/usr/bin/env python3
""" wait_random module """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ ret random number btw 0 & max_dela """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
