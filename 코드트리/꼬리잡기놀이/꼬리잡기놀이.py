from collections import deque

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
score = 0
round = 0
dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]


def in_range(x: int, y: int):
    return x in range(n) and y in range(n)


def move():
    visited = [[False for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if visited[x][y]: continue
            if board[x][y] != 3: continue
            last_number = 4
            queue = deque()
            queue.append([x, y, 3])
            visited[x][y] = True
            while queue:
                qx, qy, number = queue.popleft()
                for dx, dy in zip(dxs, dys):
                    nx, ny = qx + dx, qy + dy
                    if nx == x and ny == y and number == 1:
                        board[x][y] = 1
                    if not in_range(nx, ny) or visited[nx][ny] or board[nx][ny] == 0: continue
                    next_number = board[nx][ny]
                    if number == 3 and next_number == 2:
                        board[qx][qy] = 4
                        board[nx][ny] = 3
                        visited[nx][ny] = True
                        queue.append([nx, ny, next_number])
                    elif number == next_number == 2:
                        visited[nx][ny] = True
                        queue.append([nx, ny, next_number])
                    elif number == 2 and next_number == 1:
                        board[nx][ny] = 2
                        visited[nx][ny] = True
                        queue.append([nx, ny, next_number])
                    elif number == 1 and next_number == 4:
                        board[nx][ny] = 1
                        visited[nx][ny] = True


def shoot():
    ball = [(round // n) % 4, round % n]
    direction, line = ball
    # print(f'ball: {ball}')
    if direction == 0:
        start = [line, 0]
    elif direction == 1:
        start = [n - 1, line]
    elif direction == 2:
        start = [line, n - 1]
    else:
        start = [0, line]
    print(direction)
    ball_x, ball_y = start
    # print(start)
    while in_range(ball_x, ball_y):
        if board[ball_x][ball_y] in range(1, 4):
            change_direction(ball_x, ball_y)
            break
        ball_x += dxs[direction]
        ball_y += dys[direction]


def change_direction(x: int, y: int):
    # print(x, y)
    global score
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = deque()
    head_pos, tail_pos = [], []
    queue.append([x, y, 1])
    visited[x][y] = True

    while queue:
        qx, qy, distant = queue.popleft()
        if board[qx][qy] == 1:
            score += distant * distant
            head_pos = [qx, qy]
        elif board[qx][qy] == 3:
            tail_pos = [qx, qy]
        for dx, dy in zip(dxs, dys):
            nx, ny = qx + dx, qy + dy
            if not in_range(nx, ny) or visited[nx][ny] or board[nx][ny] not in range(1, 4): continue
            if board[nx][ny] == 1 and board[qx][qy] == 3: continue
            queue.append([nx, ny, distant + 1])
            visited[nx][ny] = True
    # print(head_pos, tail_pos)

    board[head_pos[0]][head_pos[1]] = 3
    board[tail_pos[0]][tail_pos[1]] = 1


if __name__ == '__main__':
    for _ in range(k):
        move()
        # for row in board:
        #     print(row)
        shoot()
        round += 1

    print(score)
    # for row in board:
    #     print(row)
