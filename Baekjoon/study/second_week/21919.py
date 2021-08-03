import math

def gcd(x,y):
    while y:
        x, y = y , x % y
    return x

def lcm(x,y):
    return (x*y) // gcd(x,y)

def prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

n = int(input())
lst = list(map(int,input().split()))

prime_lst = []

for num in lst:
    if prime(num):
        prime_lst.append(num)

if len(prime_lst) == 0:
    print(-1)
else:
    while True:
        prime_lst.append(lcm(prime_lst.pop(),prime_lst.pop()))
        if len(prime_lst) == 1:
            print(prime_lst[0])
            break

