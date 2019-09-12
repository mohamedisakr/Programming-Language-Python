from math import factorial

n = int(input())
for i in range(1, n+1):
    c = 1
    for j in range(1, i+1):
        print(c, end=' ')
        c = int((c*(i-j))/j)
    print()

# Method 1
'''
from math import factorial
n = int(input())
print()
for i in range(n):
    for j in range(i+1):
        print(factorial(i)//((factorial(j))*(factorial(i-j))), end=' ')
    print()
'''
