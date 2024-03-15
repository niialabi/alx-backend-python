#!/usr/bin/env python3
""" string float to string float square module """

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ takes string and float and ret float, string square """
    return (k, v ** 2)
