#!/usr/bin/env python3
"""
This module contains an asynchronous function that
spawn wait_random n times with the specified max_delay.
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """"""
    delays = await asyncio.gather(
            *list(map(lambda _: wait_random(max_delay), range(n))))
    return sorted(delays)
