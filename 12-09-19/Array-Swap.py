a = [int(x) for x in input().split()]
n = len(a)

if n % 2 == 0:
    print(a[n//2:]+a[:n//2])
else:
    print(a[n//2+1:]+a[n//2:n//2+1]+a[:n//2])
