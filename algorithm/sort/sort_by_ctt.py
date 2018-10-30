"""
冒泡/插入/选择 时间复杂度 O(n^2) 基于比较
快排/归并 O(nLogn) 基于比较
桶，计数，基数 O(n) 不基于比较

评价排序算法

执行效率

1. 依照有序程度(有序度)，同一算法可能有最好情况，最坏情况，平均情况。
2. 不同阶比较阶，同一阶比较，系数，常数，低阶
3. 比较次数和交换次数

稳定性

内存消耗
"""


def get_order_degree(items):
    """
    获取有序度
    """
    order_count = 0
    items_len = len(items)
    for i in range(0, items_len - 1):
        for j in range(i + 1, items_len):
            if items[i] < items[j]:
                order_count += 1
    return order_count


def bubble_sort_unoptimized(items):
    """
    冒泡排序
    """
    items_len = len(items)
    for i in range(1, items_len):
        for j in range(1, items_len):
            if items[j - 1] > items[j]:
                items[j - 1], items[j] = items[j], items[j - 1]
    return items


def bubble_sort(items):
    """
    冒泡排序
    最好 O(n)
    最坏 O(n^2)
    """
    items_len = len(items)
    for i in range(1, items_len):
        has_swap = False
        for j in range(1, items_len):
            if items[j - 1] > items[j]:
                has_swap = True
                items[j - 1], items[j] = items[j], items[j - 1]
        if not has_swap:
            break
    return items


def bubble_sort_not_std(items):
    items_len = len(items)
    for i in range(items_len):
        for j in range(i + 1, items_len):
            if items[i] > items[j]:
                items[i], items[j] = items[j], items[i]
    return items


def insertion_sort(items):
    """
    感觉 list 类型不太适合用insertion sort
    还是其他语言里面的数组来表示会好点
    """
    print(items)
    raise NotImplementedError


def get_min_and_index(items):
    item = min(items)  # O(n)
    idx = items.index(item)  # O(1)
    return idx, item


def selection_sort(items):
    items_len = len(items)
    for i in range(items_len):
        min_idx, min_item = get_min_and_index(items[i:])
        items[i], items[i + min_idx] = items[i + min_idx], items[i]
    return items


def merge_sort(items):
    # Top-down implementation
    # Bottom-up implementation
    # Top-down implementation using lists
    # Bottom-up implementation using lists
    return items


def quick_sort(items):
    return items


def counting_sort(items):
    return items


def bucket_sort(items):
    return items


def radix_sort(items):
    return items


def std_sorted(items):
    return sorted(items)
