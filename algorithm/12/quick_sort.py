'''
@Date      : "2018-10-17"
@Author    :"HerryZhang"
#Reference :https://time.geekbang.org/column/article/41913
'''


def quick_sort(arrs):
    if len(arrs) <= 1:
        return arrs
    left = []
    right = []
    pivot = arrs.pop()
    for num in arrs:
        if num > pivot:
            right.append(num)
        else:
            left.append(num)
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == '__main__':
    raw_list = [3, 4, 5, 6, 7, 2, 4, 8, 10]
    print(raw_list)
    print(quick_sort(raw_list))
