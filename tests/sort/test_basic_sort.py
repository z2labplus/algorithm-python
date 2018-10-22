from algorithm.sort.basic_sort import (
    insertion_sort,
    bubble_sort,
    selection_sort,
    merge_sort,
    quick_sort,
    counting_sort,
)


def test_sort():
    expect_list = [1, 2, 3, 4, 5, 6]
    raw_list = [4, 5, 6, 3, 2, 1]
    assert bubble_sort(raw_list) == expect_list
    assert insertion_sort(raw_list) == expect_list
    assert selection_sort(raw_list) == expect_list
    assert merge_sort(raw_list) == expect_list
    assert quick_sort(raw_list) == expect_list
    assert counting_sort(raw_list) == expect_list
