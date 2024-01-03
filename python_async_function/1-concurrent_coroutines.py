#!/usr/bin/env python3
"""Module"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function to wait n number of times"""
    i = 0
    dic = []
    for i in range(0, n):
        result = await wait_random(max_delay)
        dic.append(result)
    return sorted(dic)
