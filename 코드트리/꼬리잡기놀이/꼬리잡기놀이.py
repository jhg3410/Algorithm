from collections import deque

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
score = 0
round = 0
line = [round // n, round % n]
dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]


def in_range(x: int, y: int):
    return x in range(n) and y in range(n)


def move():
    visited = [[False for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if board[x][y] != 3: continue
            queue = deque()
            queue.append([x, y, 3])
            visited[x][y] = True
            while queue:
                qx, qy, number = queue.popleft()
                for dx, dy in zip(dxs, dys):
                    nx, ny = qx + dx, qy + dy
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
    pass


def change_direction():
    pass


if __name__ == '__main__':
    for _ in range(k):
        move()
        shoot()
        change_direction()
        round += 1
    print(score)
    for row in board:
        print(row)