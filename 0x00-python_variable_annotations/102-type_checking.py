#!/usr/bin/env python3
"""
Type-annotated function zoom_array that takes a Tuple of integers and
returns a Tuple of integers.
"""
from typing import List, Tuple, TYPE_CHECKING


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Returns a Tuple of integers with the zoomed values of lst. """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


if (not TYPE_CHECKING):
    array = [12, 72, 91]

    zoom_2x = zoom_array(array)

    zoom_3x = zoom_array(array, 3.0)
