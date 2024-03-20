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

    Examples
    --------
    ```python
    from playground.stdlib.utils import is_iterable

    is_iterable(1)  # False
    is_iterable([1])  # True
    is_iterable("hello")  # True
    is_uterabke*("hello", include_str=False)  # False
    ```
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

    Examples
    --------
    ```python
    from playground.stdlib.utils import is_empty_iterable

    is_empty_iterable(1)  # False
    is_empty_iterable([1])  # False
    is_empty_iterable([])  # True
    is_empty_iterable("hello")  # False
    is_empty_iterable("")  # False
    is_empty_iterable("", include_str=True)  # True
    ```
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

    Examples
    --------
    ```python
    from playground.stdlib.utils import replace_empty_iterables

    replace_empty_iterables(1)  # 1
    replace_empty_iterables([1])  # [1]
    replace_empty_iterables([])  # None
    replace_empty_iterables([], empty_value=0)  # 0
    replace_empty_iterables("")  # ""
    replace_empty_iterables("", include_str=True)  # None
    replace_empty_iterables("", include_str=True, empty_value="missing")  # "missing"
    ```
    """
    if is_empty_iterable(value, include_str=include_str):
        return empty_value
    else:
        return value


def sort_iterables_by_sorted_order(
    iterable_to_sort: Iterable, sorted_order: Iterable
) -> Iterable:
    """
    Sorts iterable_to_sort by the order of sorted_order

    Parameters
    ----------
    iterable_to_sort : Iterable
        iterable to be sorted
    sorted_order : Iterable
        iterable to sort by

    Returns
    -------
    Iterable
        iterable_to_sort sorted by the order of sorted_order

    Examples
    --------
    ```python
    from playground.stdlib.utils import sort_iterables_by_sorted_order

    sort_iterables_by_sorted_order([1, 2, 3], [3, 2, 1])  # [3, 2, 1]
    sort_iterables_by_sorted_order({1, 2, 3}, [3, 2, 1])  # {3, 2, 1}
    sort_iterables_by_sorted_order(np.array([1, 2, 3]), [3, 2, 1])  # array([3, 2, 1])
    sort_iterables_by_sorted_order({"a": 1, "b": 2, "c": 3}, ["c", "b", "a"])  # {"c": 3, "b": 2, "a": 1}
    ```
    """
    # create a dictionary mapping elements to their positions in the sorted iterable
    order_dict = {elem: index for index, elem in enumerate(sorted_order)}

    if isinstance(iterable_to_sort, list):
        return sorted(iterable_to_sort, key=lambda x: order_dict.get(x, float("inf")))
    elif isinstance(iterable_to_sort, set):
        return set(
            sorted(iterable_to_sort, key=lambda x: order_dict.get(x, float("inf")))
        )
    elif isinstance(iterable_to_sort, np.ndarray):
        return np.array(
            sorted(iterable_to_sort, key=lambda x: order_dict.get(x, float("inf")))
        )
    elif isinstance(iterable_to_sort, dict):
        return dict(
            sorted(
                iterable_to_sort.items(),
                key=lambda x: order_dict.get(x[0], float("inf")),
            )
        )
    else:
        raise ValueError(
            f"Unsupported type of iterable_to_sort: {type(iterable_to_sort)}, expected list, set, np.ndarray, or dict"
        )


__all__ = [
    "is_iterable",
    "is_empty_iterable",
    "replace_empty_iterables",
    "sort_iterables_by_sorted_order",
]
