#!/usr/bin/env python3
"""
Type-annotated function to_kv that takes a string and an int OR float and
returns a tuple containing the string and the square of the int/float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing a string and the square of an int/float.
    """
    return (k, v ** 2)
