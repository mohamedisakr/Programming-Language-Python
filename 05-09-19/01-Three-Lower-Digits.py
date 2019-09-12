a = int(input())
a1 = a//100 + (a//10) % 10
a2 = (a//10) % 10 + a % 10
if a1 > a2:
    print(a2, a1, sep='')
else:
    print(a1, a2, sep='')
