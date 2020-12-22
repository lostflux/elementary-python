



def addition(a, b):
    return f"{raw_input} = {a + b}"


def subtract(a, b):
    return f"{raw_input} = {a - b}"


def multiply(a, b):
    return f"{raw_input} = {a * b}"


def divide(a, b):
    return f"{raw_input} = {a / b}"


# Driver code:
raw_input = input("Enter the operation you wish to perform \nwith a space after each complete number and operation \n")
split_input = raw_input.split()
if len(split_input) > 2:
    try:
        a = int(split_input[0])
        op = split_input[1]
        b = int(split_input[2])

        if op == "+":
            print(addition(a, b))
        elif op == "-":
            print(subtract(a, b))

        elif op == "*" or op == "x":
            print(multiply(a, b))

        elif op == "/":
            print(divide(a, b))

    except:
        print(f"An exception occured. Please make sure {raw_input} is a valid mathematical operation.")
