#!/usr/bin/env python3
"""floor of a float"""
import math


def floor(num: float) -> int:
    """returns floor of a float"""
    return math.floor(num)


import math

# floor = __import__("2-floor").floor

ans = floor(3.14)

print(ans == math.floor(3.14))
print(floor.__annotations__)
print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
