#!/usr/bin/env python3
""" safe_first_element func module """

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ takes first element of seq and returns any/none """
    if lst:
        return lst[0]
    else:
        return None
