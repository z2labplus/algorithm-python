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
    '''
    求平方根，精确到小数点后6位
    '''
    low = 0
    mid = x / 2
    high = x
    while abs(mid ** 2 - x) > 0.000001:
        if mid ** 2 < x:
            low = mid
        else:
            high = mid
        mid = (low + high) / 2
    return mid


if __name__ == '__main__':
    print(sqrt(11))
