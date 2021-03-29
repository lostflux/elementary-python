# Trials
# #include <stdio.h>

# CHECK OUT PYTHON 3.9.0 DOCUMENTATION
# CHECK OUT Harvard CS-50 Documentation
import time
from PIL import Image, ImageFilter
import re
print("Hello world!")
# counter = 0
#
# counter += 1
# print(counter)
#
# counter = counter + 1
# print(counter)

# counter++     # Not allowed in Python
# print(counter)

x, y = 1, 2

""" C Code:"""
# if (x < y)
# {
#   printf("x is less than y)
# }
# else if (x > y)
# {
#   printf("x is less than y")
# }
# else
# {
# printf("x is equal to y")
# }


"""Python Code:"""
# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is less than y")
# else:
#     print("x is equal to y")

"""C Code: """
# while (true)
# {
#    printf("Hello, world!)
# }

"""Python Code: """
# while True:
#     print("Hello, world!")
#     break

"""C Code: """
# int i = 0;
# while (i < 3)
# {
#     printf("Hello, world!");
#     i++;
# }


"""Python Code: """
# i = 0
# while i < 3:
#     print("Hello, world!")
#     i += 1

"""C Code: """
# for (int i = 0; i < 3, i++)
# {
#     printf(i)
# }

"""Python Code: """
# for i in [0, 1, 2]:
#     print(i)
# for i in range(3):
#     print(i)
#     print(type(i))
# for i in range(1, 6, 2):
#     print(i)

"""Python complex data-structures:"""
# Range, Lists, Tuples, Sets, Dictionaries
# Sets can't have duplicates. Python takes care of removing duplicates

def files():
    before = Image.open("bridge.bmp")
    after = before.filter(ImageFilter.BoxBlur(10))
    after.save("out.bmp")


words = set()
def load(dictionary):
    file = open(dictionary, "r")
    for line in file:
        # print(line)
        for block in line.rstrip().split():
            cleaned_words = re.findall('[a-z A-Z 0-9]+', block)
            # print(cleaned_words)
            for word in cleaned_words:
                words.add(word)
    file.close()
    return sorted(words)

def check(word):
    return word in words

def size(*, words, n):
    # for i in range(n):
    #     print(i)
    return len(words)

def unload():
    return True


print("{'x', 'int', '1', 'return', 'i', 'def', 'split', 'map', 'phi', 'in', 'for', 'print', 'input', 'float,', 'n', 'range', 'x,'}")
print(load("dictionary.py"))
# print(check("def"))
print(size(words=words, n=5))

def input_stuff():
    answer = input("Enter a string: ")
    print(f"Hello, {answer}")
    print("Hello, {0}".format(answer))


# input_stuff()
