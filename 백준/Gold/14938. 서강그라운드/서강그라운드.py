n, m, r = map(int, input().split())

itemCounts = list(map(int, input().split()))
itemCounts.insert(0, 0)

distances = [[16]*(n+1) for _ in range(n+1)]

for _ in range(r):
    a, b, distance = map(int, input().split())
    distances[a][b] = distance
    distances[b][a] = distance


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j]) 


answer = 0
for region in range(1, n+1):
    itemCount = itemCounts[region]
    for other in range(1, n+1):
        if region == other: 
            continue
        if distances[region][other] <= m: 
            itemCount += itemCounts[other]
    answer = max(answer, itemCount)

print(answer)