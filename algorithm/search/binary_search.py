"""
python3.6.4
@Date      : "2018-10-24"
@Author    :"HerryZhang"
#Reference :https://time.geekbang.org/column/article/42520
"""


def binary_search(items, val):
    """
    二分查找
    """
    return binary_search_inner(items, 0, len(items) - 1, val)


def binary_search_inner(items, low, high, value):
    if low > high:
        return -1
    mid = low + ((high - low) >> 1)
    if items[mid] == value:
        return mid
    elif items[mid] < value:
        return binary_search_inner(items, mid + 1, high, value)
    else:
        return binary_search_inner(items, low, mid - 1, value)


def sqrt(x):
    pass
