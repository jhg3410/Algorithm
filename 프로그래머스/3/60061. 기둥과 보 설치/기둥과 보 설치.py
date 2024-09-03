# 기둥 설치 유무를 가진다.
board_column = []
# 보 설치 유무를 가진다.
board_row = []
n = -1


def solution(_n, build_frames):
    global board_column, board_row, n

    n = _n
    board_column = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    board_row = [[False for _ in range(n + 1)] for _ in range(n + 1)]

    for _x, _y, a, b in build_frames:
        x, y = n - _y, _x

        if a == 0:
            if b == 1:
                build_column(x, y)
            else:
                delete_column(x, y)
        else:
            if b == 1:
                build_row(x, y)
            else:
                delete_row(x, y)

    return get_result()


def build_column(x, y):
    board_column[x][y] = True
    is_ok = check_is_ok()
    if not is_ok:
        board_column[x][y] = False


def build_row(x, y):
    board_row[x][y] = True
    is_ok = check_is_ok()
    if not is_ok:
        board_row[x][y] = False


def delete_column(x, y):
    board_column[x][y] = False
    is_ok = check_is_ok()
    if not is_ok:
        board_column[x][y] = True


def delete_row(x, y):
    board_row[x][y] = False
    is_ok = check_is_ok()
    if not is_ok:
        board_row[x][y] = True


def check_is_ok():
    for x in range(n - 1, -1, -1):
        for y in range(n + 1):
            is_column_ok = True
            is_row_ok = True
            # 기둥이 있다면
            if board_column[x][y]:
                is_column_ok = False
                # 아래가 기둥이면 괜찮다.
                if board_column[x + 1][y]: is_column_ok = True
                # 왼쪽에 보가 있다면 괜찮다.
                if y > 0 and board_row[x][y - 1]: is_column_ok = True
                # 보가 있다면 괜찮다.
                if board_row[x][y]: is_column_ok = True
            # 보가 있다면
            if board_row[x][y]:
                is_row_ok = False
                # 아래가 기둥이면 괜찮다.
                if board_column[x + 1][y]: is_row_ok = True
                # 오른쪽 아래가 기둥이면 괜찮다.
                if board_column[x + 1][y + 1]: is_row_ok = True
                # 양쪽에 보가 있다면 괜찮다.
                if board_row[x][y - 1] and board_row[x][y + 1]: is_row_ok = True

            if is_column_ok and is_row_ok:
                continue
            return False

    return True


def get_result():
    result = []

    # print("기둥------------")
    # for row in board_column:
    #     print(row)
    # print("보----------")
    # for row in board_row:
    #     print(row)
    # print("--------------------")
    for y in range(n + 1):
        for x in range(n, -1, -1):
            if board_column[x][y]:
                result.append([y, n - x, 0])
            if board_row[x][y]:
                result.append([y, n - x, 1])

    return result


if __name__ == '__main__':
    pass
print(solution(_n=5,
               build_frames=[[0, 0, 0, 1], [0, 1, 0, 1], [0, 2, 0, 1], [0, 3, 0, 1],
                             [0, 4, 0, 1], [0, 5, 1, 1], [0, 1, 1, 1], [0, 0, 0, 0]]))
