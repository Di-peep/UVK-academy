import random

import pytest

from functions import is_symmetrical


@pytest.fixture
def random_symmetrical_word_fixture():
    return random.choice(["mama", "polipoli", "yoyo"])


def test_is_symmetrical_1(random_symmetrical_word_fixture):
    assert is_symmetrical(random_symmetrical_word_fixture)


def test_is_symmetrical_2(random_symmetrical_word_fixture):
    assert is_symmetrical(random_symmetrical_word_fixture)


@pytest.fixture
def random_asymmetrical_word_fixture():
    return random.choice(["123", "qwerty", "asymmetrical"])


def test_is_not_symmetrical_1(random_asymmetrical_word_fixture):
    assert not is_symmetrical(random_asymmetrical_word_fixture)


def test_is_not_symmetrical_2(random_asymmetrical_word_fixture):
    assert not is_symmetrical(random_asymmetrical_word_fixture)
