import sys
input = sys.stdin.readline
n, m, b = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
dic = {}
for h in range(257):
    bot = top = 0
    for i in range(n):
        for j in range(m):
            if lst[i][j] > h:
                top += lst[i][j] - h
            else:
                bot += h - lst[i][j]
    
    if b + top < bot:
        continue
    time = bot + (top *2)
    dic[time] = h
t = min(dic)
max_h = dic.get(t)
print(t,max_h)