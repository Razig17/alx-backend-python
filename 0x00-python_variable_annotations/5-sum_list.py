#!/usr/bin/env python3
"""
type-annotated function sum_list which takes a list of floats as argument and
returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of float numbers as a float.
    """
    return sum(input_list)
