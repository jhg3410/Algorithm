n, m, h, k = map(int, input().split())
# 술래 위치
taker = [n // 2, n // 2]
# 술래 방향(처음엔 위)
taker_d = 0
# 도망자 위치
runners = [[[] for _ in range(n)] for _ in range(n)]
# 나무 위치
trees = [[False for _ in range(n)] for _ in range(n)]
for _ in range(m):
    _x, _y, _d = map(int, input().split())
    runners[_x - 1][_y - 1].append(_d)
for _ in range(h):
    _x, _y = map(int, input().split())
    trees[_x - 1][_y - 1] = True

score = 0
turn = 1


def in_range(x: int, y: int):
    return x in range(n) and y in range(n)


def move_runner():
    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]
    tmp_board = [[[] for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if abs(x - taker[0]) + abs(y - taker[1]) > 3:
                for direction in runners[x][y]:
                    tmp_board[x][y].append(direction)
                continue
            if not runners[x][y]:
                continue
            for direction in runners[x][y]:
                nx, ny = x + dxs[direction], y + dys[direction]
                if not in_range(nx, ny):
                    nd = (direction + 2) % 4
                else:
                    nd = direction
                nx, ny = x + dxs[nd], y + dys[nd]
                if nx == taker[0] and ny == taker[1]:
                    nx, ny = x, y
                tmp_board[nx][ny].append(nd)

    for x in range(n):
        for y in range(n):
            runners[x][y] = tmp_board[x][y]


offsets = sum([[i, i] for i in range(1, n)], []) + [n - 1]
offsets_reverse = [n - 1] + sum([[i, i] for i in range(n - 1, 0, -1)], [])
is_reversed = False
current_offset = 0
current_offset_idx = 0


def move_taker():
    global taker_d, taker, current_offset_idx, current_offset, is_reversed
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    r_dxs, r_dys = [1, 0, -1, 0], [0, 1, 0, -1]
    current_dxs, current_dys = (r_dxs, r_dys) if is_reversed else (dxs, dys)
    current_offsets = offsets_reverse if is_reversed else offsets

    taker_x, taker_y = taker[0], taker[1]
    taker_x += current_dxs[taker_d]
    taker_y += current_dys[taker_d]
    taker = [taker_x, taker_y]
    if (taker_x == 0 and taker_y == 0) or (taker_x == n // 2 and taker_y == n // 2):
        # 초기화
        is_reversed = not is_reversed
        current_offset = current_offset_idx = 0
        taker_d = 0
        return

    current_offset += 1
    if current_offset == current_offsets[current_offset_idx]:
        current_offset_idx += 1
        current_offset = 0
        taker_d = (taker_d + 1) % 4


def catch():
    global score
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    r_dxs, r_dys = [1, 0, -1, 0], [0, 1, 0, -1]
    current_dxs, current_dys = (r_dxs, r_dys) if is_reversed else (dxs, dys)

    taker_x, taker_y = taker[0], taker[1]
    for i in range(3):
        nx = taker_x + i * current_dxs[taker_d]
        ny = taker_y + i * current_dys[taker_d]
        if not in_range(nx, ny): return
        if trees[nx][ny]: continue
        if not runners[nx][ny]: continue
        score += len(runners[nx][ny]) * turn
        runners[nx][ny].clear()


if __name__ == '__main__':
    for _ in range(k):
        move_runner()
        move_taker()
        catch()
        turn += 1
    print(score)