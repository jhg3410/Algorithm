def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*factorial(n-1)

n , k = map(int,input().split())

if k < 0:
    print(0)
if k>n:
    print(0)
else: 
    print(int(factorial(n) / (factorial(k) * factorial(n-k))))