#!/usr/bin/env python3
""" async_comprehension module """
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """ async comp returns list of floats """
    return [gen_input async for gen_input in async_generator()]
