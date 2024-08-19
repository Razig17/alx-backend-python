#!/usr/bin/env python3
"""
This module contains an asynchronous function that
spawn wait_random n times with the specified max_delay.
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns task_wait_random n times with the specified max_delay"""
    delays = await asyncio.gather(
            *list(map(lambda _: task_wait_random(max_delay), range(n))))
    return sorted(delays)
