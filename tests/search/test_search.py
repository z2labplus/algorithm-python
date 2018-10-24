from algorithm.search.binary_search import binary_search


def test_search():
    items_to_be_sorted = [8, 11, 19, 23, 27, 33, 45, 55, 67, 98]
    assert binary_search(items_to_be_sorted, 11)
