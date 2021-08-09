from collections import deque
import copy
n = int(input())
lst_1 = [list(input()) for _ in range(n)]
lst_2 = copy.deepcopy(lst_1)
for i in range(n):
    for j in range(n):
        if lst_2[i][j] == 'R':
            lst_2[i][j] = 'G'

dx = [1,-1,0,0]
dy = [0,0,1,-1]

visited_1 = [[0 for _ in range(n)] for i in range(n)]
visited_2 = [[0 for _ in range(n)] for i in range(n)]
def bfs(x,y,lst,visited):
    queue = deque()
    queue.append([x,y])
    visited_1[x][y] == 1
    while queue:
        a,b =queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if  (0 <= nx < n) and (0 <= ny < n):
                if lst[a][b] == lst[nx][ny]:
                    if visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        queue.append([nx,ny])

cnt_1 = 0
cnt_2 = 0
for i in range(n):
    for j in range(n):
        if visited_1[i][j] == 0:
            bfs(i,j,lst_1,visited_1)
            cnt_1 += 1
            
for i in range(n):
    for j in range(n):
        if visited_2[i][j] == 0:
            bfs(i,j,lst_2,visited_2)
            cnt_2 += 1

print(cnt_1,cnt_2)
