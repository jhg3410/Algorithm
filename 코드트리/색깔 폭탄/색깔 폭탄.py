from collections import deque

EMPTY = -10 ** 10
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
score = 0


def in_range(x: int, y: int):
    return x in range(n) and y in range(n)


def delete_bomb():
    global score
    find_pos = find_bomb()
    for x, y in find_pos:
        board[x][y] = EMPTY

    score += len(find_pos) * len(find_pos)


def find_bomb():
    dxs = [1, -1, 0, 0]
    dys = [0, 0, 1, -1]
    visited = [[False for _ in range(n)] for _ in range(n)]
    find = []
    find_red_count = 0
    for x in range(n - 1, -1, -1):
        for y in range(n):
            if board[x][y] < 1: continue
            red_visited = [[False for _ in range(n)] for _ in range(n)]
            queue = deque()
            queue.append([x, y])
            color = board[x][y]
            visited[x][y] = True
            stored = []
            red_count = 0

            while queue:
                qx, qy = queue.popleft()
                stored.append([qx, qy])
                for dx, dy in zip(dxs, dys):
                    nx, ny = qx + dx, qy + dy
                    if not in_range(nx, ny): continue
                    if visited[nx][ny]: continue
                    if red_visited[nx][ny]: continue
                    if board[nx][ny] == 0:
                        queue.append([nx, ny])
                        red_visited[nx][ny] = True
                        red_count += 1
                    elif board[nx][ny] == color:
                        queue.append([nx, ny])
                        visited[nx][ny] = True
            if len(stored) < 2: continue
            if len(stored) > len(find):
                find = stored
                find_red_count = red_count
            elif len(stored) == len(find):
                if red_count < find_red_count:
                    find = stored
                    find_red_count = red_count
    return find


def operate_gravity():
    for y in range(n):
        for x in range(n - 2, -1, -1):
            if board[x][y] < 0: continue
            px = x
            nx = x + 1
            while nx < n:
                if board[nx][y] == EMPTY:
                    board[nx][y], board[px][y] = board[px][y], EMPTY
                    px = nx
                    nx += 1
                else:
                    break


# 반시계 90도 회전
def rotate():
    new_board = [[0 for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            new_board[x][y] = board[y][n - x - 1]

    for x in range(n):
        for y in range(n):
            board[x][y] = new_board[x][y]


def is_end():
    find = find_bomb()
    return not find


if __name__ == '__main__':
    while not is_end():
        delete_bomb()
        operate_gravity()
        rotate()
        operate_gravity()
    print(score)
