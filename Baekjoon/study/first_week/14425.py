import sys
input = sys.stdin.readline

n, m = map(int,input().split())
lst_n = [input() for _ in range(n)]
lst_m = [input() for _ in range(m)]

cnt = 0
for i in lst_m:
    if i in lst_n:
        cnt += 1
        
print(cnt)