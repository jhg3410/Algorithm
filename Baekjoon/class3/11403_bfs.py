from collections import deque

n = int(input())
ans_lst = []
num_lst = [list(map(int,input().split())) for i in range(n)]


def bfs(v):
    visited = [0 for _ in range(n)]
    queue = deque([v])

    while queue:
        index = queue.popleft()
        for a,b in enumerate(num_lst[index]):
            if visited[a] == 0 and b == 1:
                queue.append(a)
                visited[a] = 1
    return visited    

for i in range(n):
    ans_lst.append(bfs(i))


for i in range(n):
    for j in range(n):
        print(ans_lst[i][j], end= " ")
    print()