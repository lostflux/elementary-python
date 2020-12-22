# What is the runtime for each of the following functions?
def func1(n):  # O(n)
    for i in range(n):
        print(i)


def func2(n):  # O(n)
    for i in range(2, n):
        print(i)


def func3(n):  # O(n^2)
    for i in range(n):
        for j in range(n):
            print(i * j)


def func4(glist):  # O(n^3)
    for x in glist:
        for y in glist:
            if x != y:
                for z in glist:
                    if z != x and z != y:
                        print([x, y, z])


def func5(glist):  # O(n)
    i = 0
    for x in range(0, 2):
        for j in range(len(glist)):
            if glist[j] == x:
                i = i + 1
    return i


def func6(n):  # O(log(n))
    i = n
    while i >= 1:
        print(i % 10)
        i = i // 10


def func7(n):  # O(nlog(n))
    for i in range(0, n):
        func6(n)

def func8(n):  # O(log(n))
    i = 1
    while i < n:
        i = i * 2
        print(i)

def func9(glist, n):  # O(n * (len(glist) + n))
    for i in range(n):  # n
        glist.insert(0, i)  # len(glist) + n


def func10(n):  # O(n)
    i = 0
    while i < n:
        i = i + 1

    while i > 0:
        i = i - 1


def func11(n):  # O(n)
    i = 0
    while i < n:
        i = i + 1

    if i > 10:
        print(i)




