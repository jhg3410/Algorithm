n = int(input())
ans_lst = []
num_lst = [list(map(int,input().split())) for i in range(n)]
visited = [0 for _ in range(n)]


def dfs(v):
    for i in range(n):
        if visited[i] == 0 and num_lst[v][i] == 1:
            visited[i] = 1
            dfs(i)    

for i in range(n):
    dfs(i)
    ans_lst.append(visited)
    visited = [0 for _ in range(n)]


for i in range(n):
    for j in range(n):
        print(ans_lst[i][j], end= " ")
    print()