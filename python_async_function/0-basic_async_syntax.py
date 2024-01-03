#!/usr/bin/env python3
"""Module"""
from random import uniform
from asyncio import sleep


async def wait_random(max_delay: int = 10):
    """Asynchronous coroutine"""
    delay = uniform(0, max_delay)
    await sleep(delay)
    return delay
