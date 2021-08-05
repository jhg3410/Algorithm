from collections import deque

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

queue = deque()

m, n, h = map(int,input().split())
lst = [[list(map(int,input().split())) for i in range(n)] for _ in range(h)]

def bfs():
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nz < h) and (0 <= nx < n) and (0 <= ny < m):
                if lst[nz][nx][ny] == 0:
                    queue.append([nz,nx,ny])
                    lst[nz][nx][ny] = lst[z][x][y] + 1


for i in range(h):
    for j in range(n):
        for k in range(m):
            if lst[i][j][k] == 1:
                queue.append([i,j,k])

bfs()

result = 0
cant_eat = 0
for i in lst:
    for j in i:
        for k in j:
            if k == 0:
                cant_eat = -1
            result = max(k,result)
if cant_eat == -1:
    print(-1)
elif result == 1:
    print(0)
else:
    print(result - 1)

