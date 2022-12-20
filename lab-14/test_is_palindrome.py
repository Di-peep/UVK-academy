import pytest

from functions import is_palindrome


def test_is_palindrome_pass_1():
    assert is_palindrome("404")


def test_is_palindrome_pass_2():
    assert is_palindrome("level")


def test_is_palindrome_pass_3():
    assert is_palindrome("noon")


@pytest.mark.xfail
def test_is_palindrome_fail_1():
    assert is_palindrome("fail")


@pytest.mark.xfail
def test_is_palindrome_fail_2():
    assert is_palindrome("ups 403")
