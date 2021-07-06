n, m, b = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(3)]
dic = {}
for h in range(257):
    bot = top = 0
    for i in range(n):
        for j in range(m):
            if lst[n][m] > h:
                top += lst[n][m] - h
            else:
                bot += h - lst[n][m]
    
    if b + top < bot:
        continue
    time = bot + (top *2)
    dic[h] = time
print(dic)