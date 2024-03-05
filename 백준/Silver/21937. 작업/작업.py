
from collections import deque


def bfs():
    global answer
    queue = deque()
    visited = [False] * (n+1)
    queue.append(findNumber)
    visited[findNumber] = True

    while queue:
        standard = queue.popleft()
        for node in board[standard]:
            if visited[node] == True: continue
            queue.append(node)
            visited[node] = True
            answer+=1



answer = 0
n, m = map(int, input().split())
board = [[] for i in range(0, n+1) ]
for i in range(0, m):
    shot, receive = map(int, input().split())
    board[receive].append(shot)

findNumber = int(input())

bfs()
print(answer)