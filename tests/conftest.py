import pytest
import random


@pytest.fixture
def items_to_be_sorted():
    items = list(range(1, 1000))
    random.shuffle(items)
    return items


@pytest.fixture
def items_expected_sorted():
    return list(range(1, 1000))
