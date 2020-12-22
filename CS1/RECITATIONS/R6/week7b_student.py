def func1(n):  # O(n)
    if n == 0:
        return 1

    res = n * func1(n-1)
    return res


def func2(n):  # O(log(n))
    if n <= 1:  # 1
        print(1)

    print(n)  # 1
    return func2(n//2)  # log(n)


def func3(n, i = 1):  # O(log(n))
    if i >= n:  # 1 once
        print(i)
        return

    print(i)  # 1
    func3(n, i*2)  # 1 * log(n)


def func4(glist, i = 0):  # O(n)
    if i == len(glist):  # 1 once
        return

    print(glist[i])  # 1
    func4(glist, i+1)  # n


def func5(glist):  # O(len(glist)^2            O(n^2)
    if len(glist) == 0:  # 1 once
        return

    print(glist[0])  # 1
    func5(glist[1:])  # len(glist) * len(glist)


def func6(glist, i=1):  # O(log(len(glist)))       O(log(n))
    if i >= len(glist):  # 1 once
        return

    print(glist[i])  # 1
    func6(glist, i*2)  # 1 * log(len(glist))

def func7(glist, i = 0, j = None): # O(log(len(glist))       O(log(m)
    if j == None:  # 1
        j = len(glist) - 1

    if i >= j:  # 1
        return

    t = (i + j) // 2  # 1
    print(t)  # 1
    func7(glist, i, t)  # log(j)

def func8(glist, i = 0):  #O(len(glist))            O(m)
    if i == len(glist):  # 1
        return []

    res = func8(glist, i+1)  # len(glist)
    res.append(glist[i] * 2)  # 1

    return res


def func9(glist, i=0):  # O(len(glist)^2)          O(m^2)
    if i == len(glist):  # 1
        return []

    res = func9(glist, i + 1)  # 1 * len(glist
    res.insert(0, glist[i] * 2)  # n * n

    return res
