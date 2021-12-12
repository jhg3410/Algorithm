import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
S,E = map(int,input().split())
tel_lst = [[]for _ in range(N+1)]

for _ in range(M):
    x,y = map(int,input().split())
    tel_lst[x].append(y)
    tel_lst[y].append(x)
visited = [-1] *(N+1)

queue = deque([S])
visited[S] = 0

while queue:
    c = queue.popleft()
    node = [c-1,c+1]
    for i in tel_lst[c]:
        node.append(i)
    for tmp in node:
        if 1<=tmp<=N and visited[tmp] == -1:
            queue.append(tmp)
            visited[tmp] = visited[c] + 1   
            if tmp == E:
                print(visited[tmp]) 
                exit()
