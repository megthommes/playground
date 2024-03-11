from typing import Any
import pytest

from playground.stdlib.utils import (
    is_empty_iterable,
    is_iterable,
    replace_empty_iterables,
)


class TestUtils:
    @pytest.mark.parametrize(
        "value, include_str, expected",
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
    def test_is_iterable(self, value: Any, include_str: bool, expected: bool) -> None:
        """
        Test the is_iterable function.

        Parameters
        ----------
        value : Any
            The value to check for iterability.
        include_str : bool
            Flag indicating whether to include strings as iterable.
        expected : bool
            The expected result of the is_iterable function.
        """
        assert is_iterable(value, include_str=include_str) == expected

    @pytest.mark.parametrize(
        "value, include_str, expected",
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
        self, value: Any, include_str: bool, expected: bool
    ) -> None:
        """
        Test the is_empty_iterable function.

        Parameters
        ----------
        value : Any
            The value to check for emptiness.
        include_str : bool
            Flag indicating whether to include strings as iterable.
        expected : bool
            The expected result of the is_empty_iterable function.
        """
        assert is_empty_iterable(value, include_str=include_str) == expected

    @pytest.mark.parametrize(
        "value, include_str, empty_value, expected",
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
        self, value: Any, include_str: bool, empty_value: Any, expected: Any
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
        expected : Any
            The expected output value.
        """

        assert (
            replace_empty_iterables(
                value, include_str=include_str, empty_value=empty_value
            )
            == expected
        )
