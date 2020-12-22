

def check_primes(L):
    status = True
    for i in L:
        if i == 1:
            status = False
            break
        else:
            for j in range(2, i):
                if i % j == 0:
                    status = False
                    break
    return status


L1 = [2, 3, 5, 7, 9]
L2 = [5, 13, 17, 19, 23]
L3 = [1, 1, 1, 1, 1, 1]
L4 = [100]
L5 = [101, 103]
print(L1, check_primes(L1))
print(L2, check_primes(L2))
print(L3, check_primes(L3))
print(L4, check_primes(L4))
print(L5, check_primes(L5))

