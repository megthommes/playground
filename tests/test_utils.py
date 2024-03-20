from typing import Any, Iterable
import pytest
import numpy as np

from playground.stdlib.utils import (
    is_empty_iterable,
    is_iterable,
    replace_empty_iterables,
    sort_iterables_by_sorted_order,
)


class TestUtils:
    @pytest.mark.parametrize(
        "value, include_str, expected_result",
        [
            ([], True, True),
            ([1], True, True),
            ("", True, True),
            ("hello", True, True),
            ("", False, False),
            ("hello", False, False),
            ((), True, True),
            ((1,), True, True),
            ({}, True, True),
            ({1}, True, True),
        ],
    )
    def test_is_iterable(
        self, value: Any, include_str: bool, expected_result: bool
    ) -> None:
        """
        Test the is_iterable function.

        Parameters
        ----------
        value : Any
            The value to check for iterability.
        include_str : bool
            Flag indicating whether to include strings as iterable.
        expected_result : bool
            The expected result of the is_iterable function.
        """
        assert is_iterable(value, include_str=include_str) == expected_result

    @pytest.mark.parametrize(
        "value, include_str, expected_result",
        [
            ([], True, True),
            ([1], True, False),
            ("", True, True),
            ("hello", True, False),
            ("", False, False),
            ("hello", False, False),
            ((), True, True),
            ((1,), True, False),
            ({}, True, True),
            ({1}, True, False),
        ],
    )
    def test_is_empty_iterable(
        self, value: Any, include_str: bool, expected_result: bool
    ) -> None:
        """
        Test the is_empty_iterable function.

        Parameters
        ----------
        value : Any
            The value to check for emptiness.
        include_str : bool
            Flag indicating whether to include strings as iterable.
        expected_result : bool
            The expected result of the is_empty_iterable function.
        """
        assert is_empty_iterable(value, include_str=include_str) == expected_result

    @pytest.mark.parametrize(
        "value, include_str, empty_value, expected_result",
        [
            ([], True, None, None),
            ([1], True, None, [1]),
            ("", True, None, None),
            ("hello", True, None, "hello"),
            ("", False, None, ""),
            ("hello", False, None, "hello"),
            ((), True, None, None),
            ((1,), True, None, (1,)),
            ({}, True, None, None),
            ({1}, True, None, {1}),
        ],
    )
    def test_replace_empty_iterables(
        self, value: Any, include_str: bool, empty_value: Any, expected_result: Any
    ) -> None:
        """
        Test the replace_empty_iterables function.

        Parameters
        ----------
        value : Any
            The input value to be tested.
        include_str : bool
            A flag indicating whether to include strings in the replacement.
        empty_value : Any
            The value to replace empty iterables with.
        expected_result : Any
            The expected output value.
        """

        assert (
            replace_empty_iterables(
                value, include_str=include_str, empty_value=empty_value
            )
            == expected_result
        )

    @pytest.mark.parametrize(
        "iterable_to_sort, expected_result",
        [
            ([3, 2, 1], [1, 2, 3]),
            ({3, 2, 1}, {1, 2, 3}),
            (np.array([3, 2, 1]), np.array([1, 2, 3])),
            ({3: "a", 2: "b", 1: "c"}, {1: "c", 2: "b", 3: "a"}),
        ],
    )
    def test_sort_iterables_by_sorted_order(
        self,
        iterable_to_sort: Iterable,
        expected_result: Iterable,
    ) -> None:
        """
        Test the sort_iterables_by_sorted_order function.

        Parameters
        ----------
        iterable_to_sort : Iterable
            The iterable to sort.
        expected_result : Iterable
            The expected result of the sort.
        """
        sorted_order = {1, 2, 3}
        if isinstance(iterable_to_sort, np.ndarray):
            assert np.array_equal(
                sort_iterables_by_sorted_order(
                    iterable_to_sort, sorted_order=sorted_order
                ),
                expected_result,
            )
        else:
            assert (
                sort_iterables_by_sorted_order(
                    iterable_to_sort, sorted_order=sorted_order
                )
                == expected_result
            )
