#!/usr/bin/env python3
"""Module"""
from typing import Union
from random import uniform


async def wait_random(max_delay: int = 10) -> Union[float, int]:
    """Asynchronous coroutine"""
    return uniform(0, max_delay)
