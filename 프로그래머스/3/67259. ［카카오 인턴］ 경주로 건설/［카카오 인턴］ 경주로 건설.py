from collections import deque


def solution(board):
    n = len(board)
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    answer = float('inf')
    q = deque()
    q.append((0,0,-1,0))
    visit = {(0,0,0):0, (0,0,1):0, (0,0,2):0, (0,0,3):0}
    while q:
        x, y, direction, cost =  q.popleft()
        for d in range(4):
            newcost = cost
            nx = x + dx[d]
            ny = y + dy[d]
            if -1 <nx < n and -1 < ny < n and board[nx][ny] != 1:
                if direction == -1:
                    newcost += 100
                elif (direction - d) % 2 == 0:
                    newcost += 100
                else:
                    newcost += 600
                if nx == n-1 and ny == n-1:
                    answer = min(answer, newcost)
                elif visit.get((nx, ny, d)) is None or visit.get((nx,ny,d)) > newcost:
                    visit[(nx, ny, d)] = newcost
                    q.append((nx, ny, d, newcost))
    return answer
