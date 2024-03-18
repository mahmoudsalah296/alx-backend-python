#!/usr/bin/env python3
"""multiple coroutines at the same time"""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n, max_delay):
    """return the list of all the delays (float values)"""
    delays = []
    for i in range(n):
        delay = await asyncio.gather(wait_random(max_delay))
        delays.append(*delay)
    return sorted(delays)
