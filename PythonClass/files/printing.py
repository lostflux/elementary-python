def print_favorite_number(name, num):
    print(name + "'s favorite number is: " + num)

def say_introduction(name, num):
    print("Hello, my name is: " + name)
    print("I am a student")


name, num = map(str, input().split())
say_introduction(name, num)
print_favorite_number(name, num)
