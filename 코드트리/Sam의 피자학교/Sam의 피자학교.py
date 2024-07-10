def inject_flour():
    min_flour = min(flours)
    for idx, flour in enumerate(flours):
        if flour == min_flour:
            flours[idx] += 1


def roll_dough():
    offset = 1
    new_board = []
    while len(flours) - offset >= len(new_board) + 1:
        tmp = [-1 for _ in range(offset)]
        for i in range(offset):
            tmp[i] = flours.pop(0)
        new_board.append(tmp)
        # print(f'roll_dough: {new_board}')
        new_board = rotate(new_board)
        offset = len(new_board[0])

    new_board.append(flours)

    max_c = max([len(row) for row in new_board])

    for row in new_board:
        for _ in range(max_c - len(row)):
            row.append(0)

    return new_board


def fold_dough():
    middle = n // 2
    tmp = flours[:middle]
    new_board = [tmp[::-1], flours[middle:len(flours)]]

    middle //= 2
    left_board = [[-1 for _ in range(middle)] for _ in range(2)]
    right_board = [[-1 for _ in range(middle)] for _ in range(2)]
    for i in range(2):
        for j in range(middle):
            left_board[i][j] = new_board[i][j]

    for i in range(2):
        for j in range(middle):
            right_board[i][j] = new_board[i][j + middle]

    left_board = rotate(rotate(left_board))

    local_folded_dough = [[-1 for _ in range(middle)] for _ in range(4)]
    for i in range(2):
        for j in range(middle):
            local_folded_dough[i][j] = left_board[i][j]

    for i in range(2):
        for j in range(middle):
            local_folded_dough[i + 2][j] = right_board[i][j]

    return local_folded_dough


# 시계방향 90도 회전
def rotate(board: list[list[int]]):
    # print(f'rotate: {board}')
    r = len(board)
    c = len(board[0])
    board_n = max(r, c)
    new_board = [[0 for _ in range(board_n)] for _ in range(board_n)]
    # 0 채우기
    for i in range(board_n):
        for j in range(board_n):
            if i < r and j < c:
                new_board[i][j] = board[i][j]
    rotated_board = [[0 for _ in range(board_n)] for _ in range(board_n)]
    # 회전
    for i in range(board_n):
        for j in range(board_n):
            rotated_board[i][j] = new_board[board_n - j - 1][i]

    remove_0_board = []
    for i in range(board_n):
        row = []
        for j in range(board_n):
            if rotated_board[i][j] == 0: continue
            row.append(rotated_board[i][j])

        if row:
            remove_0_board.append(row)

    return remove_0_board


def pull_dough(dough: list[list[int]]):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    r = len(dough)
    c = len(dough[0])

    tmp = [[-1 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            tmp[i][j] = dough[i][j]

    visited = [[False for _ in range(c)] for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if dough[x][y] == 0 or visited[x][y]: continue
            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx not in range(r) or ny not in range(c): continue
                if dough[nx][ny] == 0: continue
                if visited[nx][ny]: continue
                d = abs(dough[x][y] - dough[nx][ny]) // 5
                if dough[x][y] > dough[nx][ny]:
                    tmp[x][y] -= d
                    tmp[nx][ny] += d
                else:
                    tmp[x][y] += d
                    tmp[nx][ny] -= d

    # for row in tmp:
    #     print(f'row: {row}')
    # print("---")
    flours.clear()
    for i in range(c):
        for j in range(r - 1, -1, -1):
            if tmp[j][i] == 0: continue
            flours.append(tmp[j][i])


# def print_flours():
#     print(flours)
#     print("--------------------")


if __name__ == '__main__':
    n, k = map(int, input().split())
    flours = list(map(int, input().split()))
    count = 0
    while True:
        count += 1
        inject_flour()
        rolled_dough = roll_dough()
        pull_dough(rolled_dough)
        folded_dough = fold_dough()
        pull_dough(folded_dough)
        diff = max(flours) - min(flours)
        if diff <= k:
            break

    print(count)
