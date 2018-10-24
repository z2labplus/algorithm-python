"""
python3.6.4
@Date      : "2018-10-15"
@Author    :"HerryZhang"
#Reference :https://time.geekbang.org/column/article/41802
"""


def bubble_sort(raw_list):
    """
    冒泡排序
    """
    flag = False
    list_len = len(raw_list)
    for i in range(list_len):
        for j in range(list_len - i - 1):
            if raw_list[j] > raw_list[j + 1]:
                tmp = raw_list[j]
                raw_list[j] = raw_list[j + 1]
                raw_list[j + 1] = tmp
                flag = True
        if not flag:
            break
    return raw_list


def insertion_sort(raw_list):
    """
    插入排序
    """

    list_len = len(raw_list)
    if list_len <= 1:
        return
    for i in range(1, list_len):
        value = raw_list[i]  # 1
        for j in range(i, -1, -1):
            if raw_list[j - 1] > value:
                raw_list[j] = raw_list[j - 1]
            else:
                break
        raw_list[j] = value
    return raw_list


def selection_sort(raw_list):
    """
    选择排序
    """
    list_len = len(raw_list)
    end_border = list_len - 1
    for i in range(end_border):
        sub = i
        for j in range(i + 1, list_len):
            if raw_list[sub] > raw_list[j]:
                sub = j
        raw_list[i], raw_list[sub] = raw_list[sub], raw_list[i]
    return raw_list


def merge_sort(raw_list):
    """
    归并排序
    """
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


def quick_sort(items):
    """
    快速排序
    """
    if len(items) <= 1:
        return items
    left = []
    right = []
    pivot = items.pop()
    for num in items:
        if num > pivot:
            right.append(num)
        else:
            left.append(num)
    return quick_sort(left) + [pivot] + quick_sort(right)


def bucket_sort(items):
    """
    桶排序
    """
    maxs = max(items)
    result = [0 for i in range(maxs + 1)]
    res = []
    for i in items:
        result[i] = result[i] + 1
    for i in range(maxs + 1):
        for j in range(result[i]):
            res.append(i)
    return res


def counting_sort(items):
    """
    计数排序
    """
    maxs = max(items)
    c = [0 for i in range(maxs + 1)]
    for i in items:
        c[i] = c[i] + 1
    for i in range(1, maxs + 1):
        c[i] = c[i - 1] + c[i]

    res = [0 for i in range(len(items))]
    for i in items[::-1]:
        res[c[i] - 1] = i
        c[i] = c[i] - 1
    return res


def radix_sort(items):
    """
    基数排序
    Least Signficant Digit First(LSD)
    """
    size = len(str(max(items)))
    tmp = [[] for i in range(10)]
    n = 1
    for i in range(size):
        res = []
        for single in items:
            m = single // n % 10
            tmp[m].append(single)
        for i in range(10):
            for s in tmp[i]:
                res.append(s)
        items = res
        tmp = [[] for i in range(10)]
        n = 10 * n
    return res
