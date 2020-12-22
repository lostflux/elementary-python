def print_to_n(n):
    i = 1
    while i <= n:
        print(i)
        i += 1


def print_sum(n):
    sum_value = 0
    for i in range(n + 1):
        sum_value += i
    print(sum_value)

def sum_of_odds(n):
    sum_value = 0
    for i in range(n + 1):
        if i % 2 != 0:
            sum_value += i
    print(sum_value)


n = int(input("Enter a number"))
# print_to_n(n)
# print_sum(n)
sum_of_odds(n)
