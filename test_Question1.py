import pytest

from Question1 import number_of_differences


def test_number_of_differences1():
    assert number_of_differences(2, 3, [[1, 2, 3], [4, 5, 6]], [[1, 2, 4], [3, 5, 6]]) == 2
    assert number_of_differences(2, 2, [[1, 2], [3, 4]], [[1, 2], [3, 4]]) == 0
