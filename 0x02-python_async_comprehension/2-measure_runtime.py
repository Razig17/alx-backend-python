#!/usr/bin/env python3
"""
This module containes a coroutine that will
execute async_comprehension four times
in parallel using asyncio.gather
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Masure the execution time of 4 coroutines running concurrently"""
    start = time.time
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total = time.time - start
    return total
