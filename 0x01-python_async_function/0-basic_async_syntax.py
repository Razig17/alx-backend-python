#!/usr/bin/env python3
"""
This module contains an asynchronous function that waits for a random delay.
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """Waits for a random delay between 0 and max_delay and returns it."""

    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
