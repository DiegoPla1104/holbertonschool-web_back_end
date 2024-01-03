#!/usr/bin/env python3
from typing import List, Union
"""Module"""


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """Sums all members of the list"""
    return [k, (v * v)]
