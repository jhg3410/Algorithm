from collections import deque

# stage 각 단계 그러니깐 하나씩 이동할떄마다 전의 stage에서 현재의 stage에 1을 추가( 최단 거리를 알고 싶을땐 bfs )
def bfs(graph, start):
    visited = [False for _ in range(n+1)]
    queue = deque([start])
    stage = [0]*(n+1)      
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                stage[i]=stage[v]+1
                queue.append(i)
                visited[i] = True
    
    return sum(stage)

n,m = map(int,input().split())
lst = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int,input().split())
    lst[x].append(y)
    lst[y].append(x)


result = []

for i in range(1,n+1):
    result.append(bfs(lst,i))

print(result.index(min(result))+1)