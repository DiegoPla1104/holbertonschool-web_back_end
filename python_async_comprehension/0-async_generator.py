#!/usr/bin/env python3
"""Module"""
import random
import asyncio


async def async_generator() -> float:
    """Function o create ten floats"""
    for i in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
