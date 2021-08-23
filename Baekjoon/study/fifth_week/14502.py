from collections import deque
import copy


dx = [1,-1,0,0]
dy = [0,0,1,-1]
max_result = 0

def bfs():
    copy_lst = copy.deepcopy(lst)
    global max_result

    virus_lst = []

    for i in range(n):
        for j in range(m):
            if copy_lst[i][j] == 2:
                virus_lst.append([i,j])

    result = 0
    queue = deque()

    for virus in virus_lst:
        queue.append(virus)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            if 0 <= nx <n and 0 <= ny < m:
                if copy_lst[nx][ny] == 0:
                    copy_lst[nx][ny] = 2
                    queue.append([nx,ny])

    for q in copy_lst:
        for j in q:
            if j == 0:
                result += 1
    max_result = max(max_result, result)


def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 0: 
                lst[i][j] = 1
                wall(cnt + 1)
                lst[i][j] = 0

n, m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]

wall(0)
print(max_result)