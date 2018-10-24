"""
python3.6.4
@Date      : "2018-10-24"
@Author    :"HerryZhang"
#Reference :https://time.geekbang.org/column/article/42520
"""


def bin_search(items, val):
    """
    二分查找
    """
    return bin_search_inner(items, 0, len(items) - 1, val)


def bin_search_inner(items, low, high, value):
    if low > high:
        return -1
    mid = low + ((high - low) >> 1)
    if items[mid] == value:
        return mid
    elif items[mid] < value:
        return bin_search_inner(items, mid + 1, high, value)
    else:
        return bin_search_inner(items, low, mid - 1, value)


def sqrt(x):
    pass


if __name__ == "__main__":
    items_to_be_sorted = [8, 11, 19, 23, 27, 33, 45, 55, 67, 98]
    print(bin_search(items_to_be_sorted, 11))
