#!/usr/bin/env python3
"""
This module contains an asynchronous function that
spawn wait_random n times with the specified max_delay.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> list[float]:
    """"""
    delays: list[float] = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))
    return delays
