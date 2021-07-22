import sys
sys.setrecursionlimit(2502)
def dfs(lst,x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < m):
            if lst[nx][ny] == 1:
                lst[nx][ny] = 0
                dfs(lst,nx,ny)
    
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
                dfs(lst,i,j)
                cnt += 1
    print(cnt)