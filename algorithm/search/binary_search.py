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


def binary_search_first(items, val):
    '''
    二分查找寻找第一个值等于指定值
    '''
    low = 0
    high = len(items) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if items[mid] > val:
            high = mid - 1
        elif items[mid] < val:
            low = mid + 1
        else:
            if mid == 0 or items[mid - 1] != val:
                return mid
            else:
                high = mid - 1
    return False


def binary_search_last(items, val):
    '''
    二分查找寻找最后一个值等于指定值
    '''
    low = 0
    high = len(items) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if items[mid] > val:
            high = mid - 1
        elif items[mid] < val:
            low = mid + 1
        else:
            if mid == (len(items) - 1) or items[mid + 1] != val:
                return mid
            else:
                low = mid + 1
    return False


def binary_search_first_gte(items, val):
    '''
    二分查找寻找第一个值大于等于指定值
    '''
    low = 0
    high = len(items) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if items[mid] >= val:
            if mid == 0 or items[mid - 1] < val:
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1
    return False


def binary_search_last_lte(items, val):
    '''
    二分查找寻找最后一个值小于等于指定值
    '''
    low = 0
    high = len(items) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if items[mid] > val:
            high = mid - 1
        else:
            if mid == (len(items) - 1) or items[mid + 1] > val:
                return mid
            else:
                low = mid + 1
    return False
