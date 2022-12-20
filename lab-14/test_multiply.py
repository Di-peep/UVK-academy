import pytest

from functions import multiply


@pytest.mark.parametrize("first_multiplier, second_multiplier, expected_result", [
    (10, 20, 200),
    (-2, 11, -22),
    (-12, 1, -12),
    (3.5, 2, 7),
    (1.2, 5, 6)
])
def test_multiply(first_multiplier, second_multiplier, expected_result):
    assert multiply(first_multiplier, second_multiplier) == expected_result
