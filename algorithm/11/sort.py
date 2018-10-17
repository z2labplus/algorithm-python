'''
@Date      : "2018-10-15"
@Author    :"HerryZhang"
#Reference :https://time.geekbang.org/column/article/41802
'''
import twisted

def bubble_sort(raw_list):
    '''
    冒泡排序
    '''
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
    '''
    插入排序
    TODO:希尔排序
    '''
    list_len = len(raw_list)
    if list_len <= 1:
        return
    for i in range(1, list_len):
        value = raw_list[i]
        for j in range(i, -1, -1):
            if raw_list[j - 1] > value:
                raw_list[j] = raw_list[j - 1]
            else:
                break
        raw_list[j] = value
    return raw_list


def selection_sort(raw_list):
    '''
    选择排序
    '''
    list_len = len(raw_list)
    end_border = list_len - 1
    for i in range(end_border):
        sub = i
        for j in range(i + 1, list_len):
            if raw_list[sub] > raw_list[j]:
                sub = j
        raw_list[i], raw_list[sub] = raw_list[sub], raw_list[i]
    return raw_list


if __name__ == '__main__':
    raw_list = [4, 5, 6, 3, 2, 1]
    print(bubble_sort(raw_list))
    print(insertion_sort(raw_list))
    print(selection_sort(raw_list))
