#!/usr/bin/env python3
"""
Type-annotated function safely_get_value that takes a dictionary,
a key and an optional default value and returns the value of the key.

"""
from typing import Mapping, Union, Any, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Return the value of a key in a dictionary. """
    if key in dct:
        return dct[key]
    else:
        return default
