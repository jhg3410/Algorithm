from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
change_board = [[0 for _ in range(n)] for _ in range(n)]
change_info = dict()
score = 0
EMPTY = [0, 0]


def in_range(x: int, y: int):
    return x in range(n) and y in range(n)


def set_changed_board():
    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
    count = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if visited[x][y]: continue
            count += 1
            stand = board[x][y]
            change_info[count] = stand
            change_board[x][y] = count
            queue = deque()
            queue.append([x, y])
            visited[x][y] = True

            while queue:
                cx, cy = queue.popleft()
                for dx, dy in zip(dxs, dys):
                    nx = cx + dx
                    ny = cy + dy
                    if not in_range(nx, ny): continue
                    if visited[nx][ny]: continue
                    if board[nx][ny] == stand:
                        change_board[nx][ny] = count
                        queue.append([nx, ny])
                        visited[nx][ny] = True


def get_score():
    global score
    set_changed_board()
    dxs = [1, -1, 0, 0]
    dys = [0, 0, 1, -1]
    visited = [[False for _ in range(n)] for _ in range(n)]
    tmp_score = 0
    for x in range(n):
        for y in range(n):
            if visited[x][y]: continue
            visited[x][y] = True

            local_visited = [[False for _ in range(n)] for _ in range(n)]
            local_visited[x][y] = True

            stand = change_board[x][y]
            stand_count = 1
            info = [EMPTY.copy() for _ in range(29 * 29)]
            queue = deque()
            queue.append([stand, x, y])
            while queue:
                number, c_x, c_y = queue.popleft()
                for dx, dy in zip(dxs, dys):
                    nx = c_x + dx
                    ny = c_y + dy
                    if not in_range(nx, ny): continue
                    next_number = change_board[nx][ny]
                    if next_number == number:
                        if local_visited[nx][ny]: continue
                        queue.append([next_number, nx, ny])
                        local_visited[nx][ny] = True
                        if number == stand:
                            stand_count += 1
                            visited[nx][ny] = True
                        else:
                            info[next_number][0] += 1
                    elif number == stand:
                        info[next_number][1] += 1
                        if local_visited[nx][ny]: continue
                        queue.append([next_number, nx, ny])
                        local_visited[nx][ny] = True
                        info[next_number][0] += 1
            for idx, (count, connected) in enumerate(info):
                if count == connected == 0: continue
                tmp_score += (stand_count + count) * change_info[stand] * change_info[idx] * connected
    score += tmp_score // 2


def rotate():
    rotated_board = [[0 for _ in range(n)] for _ in range(n)]
    # 십자가 처리
    vertical, horizontal = [], []
    for i in range(n):
        vertical.append(board[i][n // 2])
    horizontal = board[n // 2]

    horizontal, vertical = vertical[:], horizontal[::-1]

    for i in range(n):
        rotated_board[i][n // 2] = vertical[i]
    rotated_board[n // 2] = horizontal

    # 작은 사각형 처리
    small_size = n // 2
    # 왼위
    small_rect = []
    for x in range(small_size):
        tmp = []
        for y in range(small_size):
            tmp.append(board[x][y])
        small_rect.append(tmp)
    rotated = sum(rotate_rect(small_rect), [])
    for x in range(small_size):
        for y in range(small_size):
            rotated_board[x][y] = rotated.pop(0)

    # 오위
    small_rect = []
    for x in range(small_size):
        tmp = []
        for y in range(small_size + 1, n):
            tmp.append(board[x][y])
        small_rect.append(tmp)
    rotated = sum(rotate_rect(small_rect), [])
    for x in range(small_size):
        for y in range(small_size + 1, n):
            rotated_board[x][y] = rotated.pop(0)

    # 왼아래
    small_rect = []
    for x in range(small_size + 1, n):
        tmp = []
        for y in range(small_size):
            tmp.append(board[x][y])
        small_rect.append(tmp)
    rotated = sum(rotate_rect(small_rect), [])
    for x in range(small_size + 1, n):
        for y in range(small_size):
            rotated_board[x][y] = rotated.pop(0)

    # 오아래
    small_rect = []
    for x in range(small_size + 1, n):
        tmp = []
        for y in range(small_size + 1, n):
            tmp.append(board[x][y])
        small_rect.append(tmp)
    rotated = sum(rotate_rect(small_rect), [])
    for x in range(small_size + 1, n):
        for y in range(small_size + 1, n):
            rotated_board[x][y] = rotated.pop(0)

    for x in range(n):
        for y in range(n):
            board[x][y] = rotated_board[x][y]


def rotate_rect(rect: list[list[int]]):
    rotated = [[0 for _ in range(n // 2)] for _ in range(n // 2)]
    for x in range(n // 2):
        for y in range(n // 2):
            rotated[x][y] = rect[n // 2 - y - 1][x]
    return rotated


if __name__ == '__main__':
    get_score()
    for _ in range(3):
        rotate()
        get_score()
    print(score)