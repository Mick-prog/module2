import os
def plus():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except ValueError:
        print("Enter only numbers")
    else:
        result = a + b
        return str(result)
def minus():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except ValueError:
        print("Enter only numbers")
    else:
        result = a - b
        return str(result)
def mult():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except ValueError:
        print("Enter only numbers")
    else:
        result = a * b
        return str(result)
def div():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except ValueError:
        print("Enter only numbers")
    else:
        result = a / b
        return str(result)


while True:
    try:
        tools = int(input(f"choose tool you want to use\n1 - calculator\n2 - show history\n3 - delete history\n: "))
    except ValueError:
        print("write only 1, 2 or 3")
    else:
        if tools == 1:
            try:
                do = input("choose action: '+' '-' '*' '/': ")
            except ValueError:
                print("Enter only numbers")
            else:
                if do == "+":
                    result = plus()
                    with open("file.txt", "a+") as file:
                        file.write(f"{result}\n")
                        print(result)
                elif do == "-":
                    result = minus()
                    with open("file.txt", "a+") as file:
                        file.write(f"{result}\n")
                        print(result)

                elif do == "*":
                    result = mult()
                    with open("file.txt", "a+") as file:
                        file.write(f"{result}\n")
                        print(result)
        
                elif do == "/":
                    result = div()
                    with open("file.txt", "a+") as file:
                        file.write(f"{result}\n")
                        print(result)
        elif tools == 2:
            with open("file.txt", "r") as file:
                history = file.read()
                print(history)
        elif tools == 3:
            os.remove("file.txt")


