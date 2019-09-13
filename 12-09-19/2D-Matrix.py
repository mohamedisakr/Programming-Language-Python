from random import randint
n = int(input('# rows'))
m = int(input('# columns'))
a = [[randint(-10,10) for i in range(m)] for j in range(n)]

# Method 1
for i in a:
    for j in i:
        print(j,end=' ')

# Method 2
for i in range(n):
    for j in range(m):
        print(a[i][j],end=' ')        