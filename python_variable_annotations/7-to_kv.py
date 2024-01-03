#!/usr/bin/env python3
from typing import Tuple, Union
"""Module"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Sums all members of the list"""
    return (k, (v * v))
