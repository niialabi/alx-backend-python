#!/usr/bin/env python3
""" make_multiplier function module """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ make multiplier funct """

    def multiply(floaty: float) -> float:
        """ returns multiplier multiplier """
        return float(floaty * multiplier)

    return multiply
