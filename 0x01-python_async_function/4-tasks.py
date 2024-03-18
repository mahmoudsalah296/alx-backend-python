#!/usr/bin/env python3
"""asyncio tasks"""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values)"""
    delays: List[float] = []
    for i in range(n):
        delay = await asyncio.gather(task_wait_random(max_delay))
        delays.append(*delay)
    return sorted(delays)
