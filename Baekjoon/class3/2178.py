from collections import deque

def bfs(x,y):
    # visited = [list(False  for _ in range(m)) for i in range(n)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque([[x,y]])
    while queue:
        x , y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <n and 0<= ny <m:
                if lst[nx][ny] == 1:
                    queue.append([nx,ny])
                    lst[nx][ny] = lst[x][y] + 1

    return lst[n-1][m-1]

n, m = map(int,input().split())
lst = [list(map(int, str(input()))) for _ in range(n)]
print(bfs(0,0))