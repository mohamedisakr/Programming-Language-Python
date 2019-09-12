from math import factorial

a = int(input())
op = input()
while op != "x" or op != "X":
    if op == "+":
        b = int(input())
        print(a+b)
    elif op == "-":
        b = int(input())
        print(a-b)
    elif op == "*":
        b = int(input())
        print(a*b)
    elif op == "/":
        b = int(input())
        if b != 0:
            print(a//b)
        else:
            print('Error division by zero')
    elif op == "%":
        b = int(input())
        print(a % b)
    elif op == "!":
        print(factorial(a))
    a = int(input())
    op = input()

print(a)
