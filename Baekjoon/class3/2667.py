from collections import deque

n = int(input())
lst = [list(map(int,str(input()))) for _ in range(n)]


dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    cnt = 1
    lst[x][y] = 0
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if lst[nx][ny] == 1:
                    lst[nx][ny] = 0
                    queue.append([nx,ny])
                    cnt += 1
    return cnt

result = []

for i in range(n):
    for j in range(n):
        if lst[i][j] == 1:
            result.append(bfs(i,j))


print(len(result))
result.sort()
for i in result:
    print(i)