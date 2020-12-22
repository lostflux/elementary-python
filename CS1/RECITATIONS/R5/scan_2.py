import random


def scan_list(list_of_numbers, new_list=None, index=0):
    if new_list is None:
        new_list = []
        index = 0

    if index > len(list_of_numbers) - 1:
        return new_list
    elif len(str(list_of_numbers[index])) == 3:
        new_list.append(list_of_numbers[index])
    index += 1
    return scan_list(list_of_numbers, new_list, index)


# list_of_numbers = [122, 174, 23, 154, 55, 0, 35, 72, 76, 83]
# print(list_of_numbers)
# print("Three-digit numbers in the list are: ", scan_list(list_of_numbers))
while True:
    list_of_numbers = []
    n = int(input("How many values in list?"))
    for i in range(n):
        list_of_numbers.append(random.randint(0, 200))

    print(list_of_numbers)
    print("Three-digit numbers in the list are: ", scan_list(list_of_numbers))
