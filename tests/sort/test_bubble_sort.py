from algorithm.sort.bubble_sort import insertion_sort, bubble_sort


def test_insertion_sort():
    expect_list = [1, 2, 3, 4, 5, 6]
    raw_list = [4, 5, 6, 3, 2, 1]
    assert bubble_sort(raw_list) == expect_list
    assert insertion_sort(raw_list) == expect_list
