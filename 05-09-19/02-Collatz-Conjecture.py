n = int(input())
print(n, end=', ')

while n > 1:
    if n % 2 == 0:
        print(n // 2, end=', ')
        n //= 2
    else:
        print((n*3)+1, end=', ')
        n = n*3+1
