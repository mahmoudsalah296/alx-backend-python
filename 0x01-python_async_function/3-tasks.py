#!/usr/bin/env python3
"""asyncio tasks"""

import asyncio
from typing import Any

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """return asyncio task"""
    return asyncio.create_task(wait_random(max_delay))
