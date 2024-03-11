from __future__ import annotations
import numpy as np
from typing import Any, Iterable


def is_iterable(value: Any, include_str: bool = True) -> bool:
    """
    Checks if value is an iterable

    Parameters
    ----------
    value : Any
        value to check
    include_str : bool = True
        Whether to include or exclude str as an iterable

    Returns
    -------
    bool
        True if value is an iterable
        False otherwise
    """
    if isinstance(value, str):
        return include_str
    elif isinstance(value, Iterable) | isinstance(value, np.ndarray):
        return True
    else:
        return False


def is_empty_iterable(value: Any, include_str: bool = False) -> bool:
    """
    Checks if value is an empty iterable

    Parameters
    ----------
    value : Any
        value to check
    include_str : bool = False
        Whether to include or exclude str as an iterable

    Returns
    -------
    bool
        True if iterable and if iterable is empty
        False otherwise
    """
    if is_iterable(value, include_str=include_str):
        try:
            iterator: Any = iter(value)
            # if it's an iterable and the next() function raises StopIteration, it's empty
            next(iterator)
            return False  # not empty
        except StopIteration:
            return True  # empty
    else:
        return False  # not an iterable


def replace_empty_iterables(
    value: Any, include_str: bool = False, empty_value: Any | None = None
) -> Any:
    """
    Replace empty iterables with {empty_value}

    Parameters
    ----------
    value : Any
        if empty iterable, value to modify
    include_str : bool = False
        Whether to include or exclude str as an iterable
    empty_value : Any | None = None
        what to replace empty iterable with

    Returns
    -------
    Any
        if empty iterable, modified value, otherwise original value
    """
    if is_empty_iterable(value, include_str=include_str):
        return empty_value
    else:
        return value


__all__ = ["is_iterable", "is_empty_iterable", "replace_empty_iterables"]
