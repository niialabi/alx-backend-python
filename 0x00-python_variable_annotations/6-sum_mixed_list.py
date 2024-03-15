#!/usr/bin/env python3
""" sums comp. list func module """

from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """ returns sum mixed list of func & float """
    return sum(input_list)
