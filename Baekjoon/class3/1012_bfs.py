from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y):    
    queue = deque()
    queue.append([x,y])
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if (0 <= nx < n) and (0 <= ny < m) and lst[nx][ny] == 1:
                queue.append([nx,ny])
                lst[nx][ny] = 0


t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split())
    lst = [[0 for i in range(m)] for j in range(n)] 

    for _ in range(k):
        y,x = map(int,input().split())
        lst[x][y] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)