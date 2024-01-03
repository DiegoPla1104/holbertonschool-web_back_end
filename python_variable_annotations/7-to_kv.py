#!/usr/bin/env python3
"""Module"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Sums all members of the list"""
    return (k, (v * v))
