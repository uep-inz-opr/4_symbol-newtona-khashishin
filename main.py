import math
n, k = input().split()
n, k = [int(n), int(k)]

if n == 0:
    print(1)
if k == 0:
    print(1)
if n == k:
    print(1)
if k > n:
    print(0)
else:
    a = math.factorial(n)
    b = math.factorial(k)
    c = math.factorial(n - k)
    symbol = a // (b*c)
    print(symbol)
