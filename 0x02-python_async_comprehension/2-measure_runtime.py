#!/usr/bin/env python3
"""task 3"""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension four times in parallel
    using asyncio.gather and return execution time"""
    start_time = time.time()
    for _ in range(4):
        await asyncio.gather(async_comprehension())
    end_time = time.time()
    return (end_time - start_time) / 4
