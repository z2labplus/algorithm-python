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
