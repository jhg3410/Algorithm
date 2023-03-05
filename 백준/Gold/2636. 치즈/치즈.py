from collections import deque
n, m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]


dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs():
    visited = [[False] *m  for _ in range(n)]
    queue = deque()
    queue.append([0,0])
    visited[0][0] = True
    cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<= nx <n and 0<= ny <m and visited[nx][ny] == False:
                if lst[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append([nx,ny])
                if lst[nx][ny] == 1:
                    visited[nx][ny] = True
                    lst[nx][ny] = 0
                    cnt += 1
    return cnt


time = 0
cheese = []
while True:
    cnt = bfs()                    
    cheese.append(cnt)
    if cnt == 0:
        break
    time += 1

print(time)
print(cheese[-2])