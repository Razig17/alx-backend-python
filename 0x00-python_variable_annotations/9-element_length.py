#!/usr/bin/env python3
"""
Type-annotated function element_length that takes an iterable of strings as
argument and returns a list of tuples containing the elements of lst and their
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing the elements of lst and their length.
    """
    return [(i, len(i)) for i in lst]
