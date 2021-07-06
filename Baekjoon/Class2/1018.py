n, m = map(int,input().split())
lst = []
for i in range(n):
        lst.append(list(input()))
mini = []
for i in range(n-7):
    for j in range(m-7):
        cnt1 = 0    # 맨 왼쪽 위가  W일때
        cnt2 = 0    # 맨 왼쪽 위가  B일때
        for a in range(i,i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if lst[a][b] == 'W':    cnt2 += 1
                    else:                   cnt1 += 1
                else:
                    if lst[a][b] == 'B':    cnt2 += 1
                    else:                   cnt1 += 1
        mini.append(cnt1)
        mini.append(cnt2)

print(min(mini))

