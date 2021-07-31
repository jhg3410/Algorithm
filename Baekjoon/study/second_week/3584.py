import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    parents = [0 for _ in range(n+1)]
    for i in range(n-1):
        a, b = map(int,input().split())
        parents[b] = a

    a, b = map(int,input().split())
    a_parents = [a]
    b_parents = [b]

    while parents[a]:
        a_parents.append(parents[a])
        a = parents[a]
    
    while parents[b]:
        b_parents.append(parents[b])
        b = parents[b]
    
    x = len(a_parents) - 1
    y = len(b_parents) - 1
    while a_parents[x] == b_parents[y]:
        x -= 1
        y -= 1
    
    print(a_parents[x+1])