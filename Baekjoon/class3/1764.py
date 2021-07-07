import sys
from bisect import bisect_left,bisect_right
input = sys.stdin.readline

n, m = map(int,input().split())
listen = [input().strip() for _ in range(n)]
see = [input().strip() for _ in range(m)]
answer = []
see.sort()
for i in listen:
    if (bisect_right(see, i) - bisect_left(see, i)) == 1:
        answer.append(i)
    else:
        continue
answer.sort()
print(len(answer))
if len(answer) > 0:
    for a in answer:
        print(a)
