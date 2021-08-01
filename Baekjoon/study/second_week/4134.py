import math
import sys
input = sys.stdin.readline

def prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

t = int(input())
for _ in range(t):
    n = int(input())
    while True:
        if prime(n):
            print(n)
            break
        else:
            n += 1


