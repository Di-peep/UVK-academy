import pytest

import functions


@pytest.mark.parametrize("line, expected_result", [
    ('[{()[]}]', True),
    ('[{]}', False),
    ('(){}[]', True),
    ('([])}', False),
    ('))((', False)
])
def test_is_balanced(line, expected_result):
    assert functions.is_balanced(line) == expected_result


def test_is_balanced_mocked_pass(mocker):
    mocker.patch('functions.is_balanced', return_value=True)
    assert functions.is_balanced("This is mocked!")


def test_is_balanced_mocked_fail(mocker):
    mocker.patch('functions.is_balanced', return_value=False)
    assert not functions.is_balanced("This is mocked!")
