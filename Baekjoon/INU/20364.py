# def solve(n):
#     lst = [n]
#     while n != 1:
#         if n %2 == 0:
#             lst.append(n // 2)
#             n = n //2
#         else:
#             lst.append((n-1) // 2)
#             n = (n-1) // 2
#     return list(reversed(lst))
import sys
input = sys.stdin.readline

n,q = map(int,input().split())
tmp = [0] * (n+1)
for i in range(q):
    x = int(input())   
    copy = x 
    a = 1
    while x != 1:
        if tmp[x] == 1:
                a = x
        if x % 2 == 0:
            x = x // 2
        else:
            x = (x-1)//2
    if a == 1:
        tmp[copy] = 1
        print(0)
    else:
        print(a)
