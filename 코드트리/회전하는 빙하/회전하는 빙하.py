from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, q = map(int, input().split())
size = 2 ** n
board = [list(map(int, input().split())) for _ in range(size)]


def in_range(x: int, y: int):
    return x in range(size) and y in range(size)


def rotate(level: int):
    for i in range(0, size, 2 ** level):
        for j in range(0, size, 2 ** level):
            # 등분한 배열 가지기
            rotate_board = [[0 for _ in range(2 ** level)] for _ in range(2 ** level)]
            for x in range(i, i + 2 ** level):
                for y in range(j, j + 2 ** level):
                    rotate_board[x - i][y - j] = board[x][y]
            # 등분한 배열 회전 후 반영
            rotated = rotate_small(rotate_board, level=level)
            for x in range(i, i + 2 ** level):
                for y in range(j, j + 2 ** level):
                    board[x][y] = rotated[x - i][y - j]


def rotate_small(rotate_board: list[list[int]], level: int):
    small_size = 2 ** level
    small_small_size = 2 ** (level - 1)
    rotated = [[0 for _ in range(small_size)] for _ in range(small_size)]
    for i in range(small_size):
        for j in range(small_size):
            # 1
            if i in range(small_small_size) and j in range(small_small_size):
                rotated[i][j + small_small_size] = rotate_board[i][j]
            # 2
            elif i in range(small_small_size) and j in range(small_small_size, small_size):
                rotated[i + small_small_size][j] = rotate_board[i][j]
            # 3
            elif i in range(small_small_size, small_size) and j in range(small_small_size, small_size):
                rotated[i][j - small_small_size] = rotate_board[i][j]
            # 4
            else:
                rotated[i - small_small_size][j] = rotate_board[i][j]
    return rotated


def melt():
    melted_board = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if board[i][j] == 0: continue
            count = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if not in_range(nx, ny): continue
                if board[nx][ny] == 0: continue
                count += 1
            if count >= 3:
                melted_board[i][j] = board[i][j]
            else:
                melted_board[i][j] = board[i][j] - 1

    for i in range(size):
        for j in range(size):
            board[i][j] = melted_board[i][j]


def get_score():
    total_amount = 0
    max_set_size = 0
    visited = [[False for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            total_amount += board[i][j]
            if visited[i][j]: continue
            if board[i][j] == 0: continue
            queue = deque()
            visited[i][j] = True
            queue.append([i, j])
            set_size = 1
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if not in_range(nx, ny): continue
                    if visited[nx][ny]: continue
                    if board[nx][ny] == 0: continue
                    visited[nx][ny] = True
                    queue.append([nx, ny])
                    set_size += 1

            max_set_size = max(max_set_size, set_size)

    return total_amount, max_set_size


if __name__ == '__main__':
    levels = list(map(int, input().split()))
    for _level in levels:
        if _level != 0:
            rotate(level=_level)
        melt()
    answer = get_score()

    print(answer[0])
    print(answer[1])
