#!/usr/bin/env python3
"""safe first"""
from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """safe first"""
    if lst:
        return lst[0]
    else:
        return None


print(safe_first_element.__annotations__)
