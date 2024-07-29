def find_answer():
    answer = 10 ** 5
    for i in range(n):
        for j in range(n):
            for left_offset in range(1, n):
                for right_offset in range(1, n):
                    if possible_rect(x=i, y=j, left_offset=left_offset, right_offset=right_offset):
                        draw_border(x=i, y=j, left_offset=left_offset, right_offset=right_offset)
                        min_diff = get_min_diff(x=i, y=j, left_offset=left_offset, right_offset=right_offset)
                        answer = min(answer, min_diff)
    return answer


def in_range(x: int, y: int):
    return x in range(n) and y in range(n)


def possible_rect(x: int, y: int, left_offset: int, right_offset: int):
    # 오른쪽 위
    if not in_range(x - right_offset, y + right_offset): return False
    # 그냥 위
    if not in_range(x - right_offset - left_offset, y + right_offset - left_offset): return False
    # 왼쪽 위
    if not in_range(x - left_offset, y - left_offset): return False

    return True


def draw_border(x: int, y: int, left_offset: int, right_offset: int):
    # 초기화
    for i in range(n):
        for j in range(n):
            border[i][j] = False
    dx = [-1, -1, 1, 1]
    dy = [1, -1, -1, 1]
    nx, ny = x, y
    for _ in range(right_offset):
        nx, ny = nx + dx[0], ny + dy[0]
        border[nx][ny] = True
    for _ in range(left_offset):
        nx, ny = nx + dx[1], ny + dy[1]
        border[nx][ny] = True
    for _ in range(right_offset):
        nx, ny = nx + dx[2], ny + dy[2]
        border[nx][ny] = True
    for _ in range(left_offset):
        nx, ny = nx + dx[3], ny + dy[3]
        border[nx][ny] = True


def get_min_diff(x: int, y: int, left_offset: int, right_offset: int):
    populations = [0, 0, 0, 0, 0, 0]
    # 2번 영역
    for i in range(x - left_offset):
        for j in range(y + right_offset - left_offset + 1):
            if border[i][j]: break
            populations[2] += board[i][j]

    # 3번 영역
    for i in range(x - right_offset + 1):
        for j in range(n - 1, y + right_offset - left_offset, -1):
            if border[i][j]: break
            populations[3] += board[i][j]

    # 4번 영역
    for i in range(x - left_offset, n):
        for j in range(y):
            if border[i][j]: break
            populations[4] += board[i][j]

    # 5번 영역
    for i in range(x - right_offset + 1, n):
        for j in range(n - 1, y - 1, -1):
            if border[i][j]: break
            populations[5] += board[i][j]

    populations[1] = total_populations - sum(populations[2:])
    return max(populations[1:]) - min(populations[1:])


if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    border = [[False for _ in range(n)] for _ in range(n)]
    total_populations = sum([
        board[q][w]
        for q in range(n)
        for w in range(n)
    ])
    print(find_answer())
