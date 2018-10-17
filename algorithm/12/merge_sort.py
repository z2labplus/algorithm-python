'''
@Date      : "2018-10-17"
@Author    :"HerryZhang"
#Reference :https://time.geekbang.org/column/article/41913
'''


def merge_sort(raw_list):
    if len(raw_list) <= 1:
        return raw_list
    mid = len(raw_list) // 2
    left = merge_sort(raw_list[:mid])
    right = merge_sort(raw_list[mid:])
    return merge(left, right)


def merge(left, right):
    pre = 0
    off = 0
    res = []
    while pre < len(left) and off < len(right):
        if left[pre] <= right[off]:
            res.append(left[pre])
            pre = pre + 1
        else:
            res.append(right[off])
            off = off + 1
    res += left[pre:]
    res += right[off:]
    return res


if __name__ == '__main__':
    raw_list = [3, 4, 5, 6, 7, 2, 4, 8, 10]
    print(raw_list)
    print(merge_sort(raw_list))
