import random


def scan_list(list_of_numbers, count=0, index=None):
    if index is None:
        index = 0
    elif index > len(list_of_numbers) - 1:
        return count
    elif len(str(list_of_numbers[index])) == 3:
        count += 1
    index += 1
    return scan_list(list_of_numbers, count, index)


list_of_numbers = []
n = int(input("How many values in list?"))
for i in range(n):
    list_of_numbers.append(random.randint(0, 200))

print(list_of_numbers)
print(f"There are {scan_list(list_of_numbers)} three-digit numbers in the list.")
