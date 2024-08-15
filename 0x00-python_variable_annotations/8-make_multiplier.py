#!/usr/bin/env python3
"""
Type-annotated function make_multiplier that takes a float multiplier and
returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a given multiplier.
    """
    def multiply(n: float) -> float:
        """
        Returns the product of a float number and a given multiplier.
        """
        return n * multiplier
    return multiply
