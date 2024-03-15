#!/usr/bin/env python3
""" Element_length func module """

from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ element leng fun """
    return [(i, len(i)) for i in lst]
