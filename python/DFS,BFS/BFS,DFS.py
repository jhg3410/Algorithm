from collections import deque

def dfs(v):
    print(v,end=" ")
    visited[v] = True
    for i in range(1,n+1):
        if visited[i] == False and graph[v][i] == True:
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v,end=" ")
        for i in range(1,n+1):
            if visited[i] == False and graph[v][i] == True:
                queue.append(i)
                visited[i] = True



n , m , v = map(int,input().split())

graph = []
for i in range(n+1):
    graph.append([False] * (n+1))

for i in range(m):
    x, y = map(int,input().split())
    graph[x][y] = True
    graph[y][x] = True

visited = [False] * (n+1)

dfs(v)
print()
visited = [False] * (n+1)
bfs(v)