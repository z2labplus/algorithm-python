import pytest

from algorithm.sort.sort_by_ctt import (
    insertion_sort,
    bubble_sort,
    selection_sort,
    merge_sort,
    quick_sort,
    counting_sort,
    bucket_sort,
    radix_sort,
    std_sorted,
    bubble_sort_unoptimized,
    get_order_degree,
    bubble_sort_not_std,
)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([1, 2, 3], 3),
        ([1, 2, 3], 3),
        ([1, 2, 3], 3),
        ([1, 2, 3], 3),
        ([1, 2, 3], 3),
        ([1, 2, 3], 3),
        ([1, 2, 3], 3),
        ([1, 2, 3, 4], 6),
    ],
)
def test_get_order_degree(test_input, expected):
    assert get_order_degree(test_input) == expected


def test_bubble_sort_unoptimized(items_to_be_sorted, items_expected_sorted):
    assert bubble_sort_unoptimized(items_to_be_sorted) == items_expected_sorted


def test_bubble_sort(items_to_be_sorted, items_expected_sorted):
    assert bubble_sort(items_to_be_sorted) == items_expected_sorted


def test_bubble_sort_not_std(items_to_be_sorted, items_expected_sorted):
    assert bubble_sort_not_std(items_to_be_sorted) == items_expected_sorted


def test_insertion_sort(items_to_be_sorted, items_expected_sorted):
    assert insertion_sort(items_to_be_sorted) == items_expected_sorted


def test_selection_sort(items_to_be_sorted, items_expected_sorted):
    assert selection_sort(items_to_be_sorted) == items_expected_sorted


def test_merge_sort(items_to_be_sorted, items_expected_sorted):
    assert merge_sort(items_to_be_sorted) == items_expected_sorted


def test_quick_sort(items_to_be_sorted, items_expected_sorted):
    assert quick_sort(items_to_be_sorted) == items_expected_sorted


def test_radix_sort(items_to_be_sorted, items_expected_sorted):
    assert radix_sort(items_to_be_sorted) == items_expected_sorted


def test_counting_sort(items_to_be_sorted, items_expected_sorted):
    assert counting_sort(items_to_be_sorted) == items_expected_sorted


def test_bucket_sort(items_to_be_sorted, items_expected_sorted):
    assert bucket_sort(items_to_be_sorted) == items_expected_sorted


def test_std_sorted(items_to_be_sorted, items_expected_sorted):
    assert std_sorted(items_to_be_sorted) == items_expected_sorted
