n, k = map(int, input().split())
# 격자판의 정보(판 색상 표시)
board = [[2 for _ in range(n + 2)]]
for _ in range(n):
    board.append([2] + list(map(int, input().split())) + [2])
board.append([2 for _ in range(n + 2)])
# 격자 판 위에 존재하는 윷
yut_board = [[[] for _ in range(n + 2)] for _ in range(n + 2)]
# 윷의 정보 (key = 윷 번호, value = 위치, 방향)
yuts = dict()
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
end = False


def start_game():
    for number in range(1, k + 1):
        move(number=number)


def move(number: int):
    x, y, d = yuts[number]
    nx, ny = x + dx[d], y + dy[d]
    # 내 위에 있는 애들 데려오기
    local_yuts = yut_board[x][y]
    move_yuts = local_yuts[local_yuts.index(number):]

    n_space = board[nx][ny]
    if n_space == 0:
        move_white(move_yuts, nx, ny)
    elif n_space == 1:
        move_red(move_yuts, nx, ny)
    else:
        move_blue(move_yuts)


def move_white(move_yuts: list[int], nx: int, ny: int):
    global end
    x, y, _ = yuts[move_yuts[0]]
    for number in move_yuts:
        # 기존 정보의 위치를 업데이트
        y_d = yuts[number][2]
        yuts[number] = [nx, ny, y_d]
        # 윷 보드 업데이트
        yut_board[x][y].remove(number)
    yut_board[nx][ny] += move_yuts
    if is_end(nx, ny):
        end = True


def move_red(move_yuts: list[int], nx: int, ny: int):
    reverse_move_yuts = move_yuts[::-1]
    move_white(reverse_move_yuts, nx, ny)


def move_blue(move_yuts: list[int]):
    standard = move_yuts[0]
    x, y, d = yuts[standard]
    nd = change_direction(d)
    # 방향 바꾸기
    yuts[standard] = [x, y, nd]

    nx, ny = x + dx[nd], y + dy[nd]
    n_space = board[nx][ny]
    if n_space == 0:
        move_white(move_yuts, nx, ny)
    elif n_space == 1:
        move_red(move_yuts, nx, ny)
    else:
        pass


def change_direction(d: int):
    return d - 1 if d % 2 == 1 else d + 1


def get_next_pos(number: int):
    x, y, d = yuts[number]
    return x + dx[d], y + dy[d]


def is_end(x: int, y: int):
    return len(yut_board[x][y]) >= 4


if __name__ == '__main__':
    for key in range(1, k + 1):
        _x, _y, _d = map(int, input().split())
        yuts[key] = [_x, _y, _d - 1]
        yut_board[_x][_y].append(key)

    for turn in range(1, 1001):
        start_game()
        if end:
            print(turn)
            exit(0)
    print(-1)
