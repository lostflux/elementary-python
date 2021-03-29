
def phi(x, n):
    n = int(n)
    for i in range(n):
        x = 1 +  1 / x
        print(x)
    return x


x, n = map(float, input().split())
print(phi(x, n))