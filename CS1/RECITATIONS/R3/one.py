def multiples(n):
    res = []
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            res.append(i)
    return res


n = int(input("Enter a number: "))
print(multiples(n))
