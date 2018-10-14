'''
python3.6.4
@Date      : "2018-10-14"
@Author    :"HerryZhang"
#Reference :https://time.geekbang.org/column/article/41440
'''


def seat(n):
    '''
    座位问题
    '''
    if n == 1:
        return 1
    return seat(n - 1) + 1


def seat_plus(n):
    '''
    座位问题
    递归变成递推
    '''
    res = 1
    for i in range(2, n + 1):
        res = res + 1
    return res


def walk(n):
    '''
    阶梯的走法
    '''
    if n == 1:
        return 1
    if n == 2:
        return 2
    return walk(n - 1) + walk((n - 2))


d = {}


def walk_plus(n):
    '''
    阶梯的走法
    解决重复计算问题
    '''
    if n == 1:
        return 1
    if n == 2:
        return 2
    if d.get(n):
        return d.get(n)
    res = walk_plus(n - 1) + walk_plus((n - 2))
    d[n] = res
    return res


def walk_no_recurrence(n):
    '''
    阶梯的走法
    递归变成递推
    '''
    if n == 1:
        return 1
    if n == 2:
        return 2
    ret = 0
    pre = 2
    prepre = 1
    for i in range(3, n + 1):
        ret = pre + prepre
        prepre = pre
        pre = ret
    return ret


if __name__ == '__main__':
    print(seat(10))
    print(seat_plus(10))
    print(walk(5))
    print(walk_plus(5))
    print(walk_no_recurrence(5))
