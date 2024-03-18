#!/usr/bin/env python3
"""multiple coroutines at the same time"""

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values)"""
    delays: List[float] = []
    for i in range(n):
        delay = await asyncio.gather(wait_random(max_delay))
        delays.append(*delay)
    return sorted(delays)
