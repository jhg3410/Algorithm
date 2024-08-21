from collections import deque

n = -1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def in_range(x: int, y: int):
    return x in range(n) and y in range(n)


def find_cross(d: int):
    return d % 2 == 0


def solution(board):
    global n
    n = len(board)
    # cost_board[x][y][d] d == 0 이면 수직 d == 1 이면 수평
    cost_board = [[[10 ** 9 for _ in range(2)] for _ in range(n)] for _ in range(n)]

    queue = deque()
    queue.append([0, 0])
    cost_board[0][0][0] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not in_range(nx, ny): continue
            if board[nx][ny] == 1: continue
            hor_ver = find_cross(i)
            # 수직이면
            if hor_ver == 1:
                new_cost = min(cost_board[x][y][1] + 100, cost_board[x][y][0] + 600)
                if x == 0 and y == 0: new_cost = 100
                if new_cost >= cost_board[nx][ny][1]: continue
                cost_board[nx][ny][1] = new_cost
                queue.append([nx, ny])
            else:
                new_cost = min(cost_board[x][y][0] + 100, cost_board[x][y][1] + 600)
                if new_cost >= cost_board[nx][ny][0]: continue
                cost_board[nx][ny][0] = new_cost
                queue.append([nx, ny])

    return min(cost_board[n - 1][n - 1])

