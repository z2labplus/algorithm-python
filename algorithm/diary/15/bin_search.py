"""
python3.6.4
@Date      : "2018-10-24"
@Author    :"HerryZhang"
#Reference :https://time.geekbang.org/column/article/42520
"""


def bin_search(arrs, val):
    '''
    二分查找
    '''
    return bin_serach_inner(arrs, 0, len(arrs) - 1, val)


def bin_serach_inner(arrs, low, high, value):
    if low > high: return -1
    mid = low + ((high - low) >> 1)
    if arrs[mid] == value:
        return mid
    elif arrs[mid] < value:
        return bin_serach_inner(arrs, mid + 1, high, value)
    else:
        return bin_serach_inner(arrs, low, mid - 1, value)


def sqrt(x):
    pass


if __name__ == '__main__':
    arrs = [8, 11, 19, 23, 27, 33, 45, 55, 67, 98]
    print(bin_search(arrs, 11))
