pre_n, pre_m = map(int, input().split())
n = max(pre_n, pre_m)
board = [['#' for _ in range(n)] for _ in range(n)]
rotate_tmp_board = [['#' for _ in range(n)] for _ in range(n)]
MAX_VALUE = 10 ** 10
answer = MAX_VALUE

for _i in range(pre_n):
    row = list(input())
    for _j in range(pre_m):
        board[_i][_j] = row[_j]


def print_info():
    print("==================")
    for row in board:
        print(row)


# def init():
#     for x in range(n):
#         for y in range(n):
#             tmp_board[x][y] = board[x][y]


def check_all_case(count: int, direction: int, pre_direction: int):
    global answer
    store_board = [['#' for _ in range(n)] for _ in range(n)]

    if count > 10:
        return
    if count > 0:
        for _ in range(direction):
            rotate()
        result = slide()
        for _ in range(4 - direction):
            rotate()
        if result == -1:
            return
        # 가능(빨강이만 출구로 나감)
        elif result == 1:
            answer = min(answer, count)
            return

    for x in range(n):
        for y in range(n):
            store_board[x][y] = board[x][y]
    for i in range(4):
        if i == pre_direction: continue
        check_all_case(count=count + 1, direction=i, pre_direction=i)
        for x in range(n):
            for y in range(n):
                board[x][y] = store_board[x][y]


def rotate():
    for x in range(n):
        for y in range(n):
            rotate_tmp_board[x][y] = board[n - y - 1][x]

    for x in range(n):
        for y in range(n):
            board[x][y] = rotate_tmp_board[x][y]


# 아래로만
def slide():
    OUT_POS = [-1, -1]
    is_red_in = False
    is_blue_in = False
    for y in range(n):
        for x in range(n - 1, -1, -1):
            if board[x][y] in ('R', 'B'):
                color = board[x][y]
                board[x][y] = '.'
                nx, ny = x, y
                while True:
                    if board[nx + 1][ny] == '#': break
                    if board[nx + 1][ny] == 'O':
                        if color == 'R':
                            is_red_in = True
                        else:
                            is_blue_in = True
                        nx, ny = OUT_POS
                        break
                    if board[nx + 1][ny] in ('R', 'B'): break
                    nx += 1
                if [nx, ny] != OUT_POS:
                    board[nx][ny] = color

    if is_blue_in: return -1
    if is_red_in: return 1
    return 0


if __name__ == '__main__':
    check_all_case(0, -1, -1)

    print(-1 if answer == MAX_VALUE else answer)
