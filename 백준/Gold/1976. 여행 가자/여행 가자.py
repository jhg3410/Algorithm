from collections import deque

def find(a):
    global parents

    if parents[a] == a:
        return a
    
    return find(parents[a])

def union(a, b):
    global parents
    parentA = find(a)
    parentB = find(b)

    if parentA > parentB:
        parents[parentA] = parentB
    else:
        parents[parentB] = parentA


n = int(input())
m = int(input())
parents = [i for i in range(n)]
relations = [list(map(int, input().split())) for _ in range(n)]


for x in range(n):
    for y, possible in enumerate(relations[x]):
        if possible:
            union(x, y)

planes = list(map(lambda x: int(x) - 1, input().split()))

pre = find(planes[0])
for road in planes[1:]:
    if pre != find(road):
        print("NO")
        exit()
    pre = find(road)


print("YES")
