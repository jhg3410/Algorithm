n, m = map(int,input().split())
unmix_lst = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    unmix_lst[a].append(b)
    unmix_lst[b].append(a)

cnt = 0
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if i in unmix_lst[j]:
            continue
        for k in range(j+1,n+1):
            if i in unmix_lst[k] or j in unmix_lst[k]:
                continue
            cnt += 1

print(cnt)