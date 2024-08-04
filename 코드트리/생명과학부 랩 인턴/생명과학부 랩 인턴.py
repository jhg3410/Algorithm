n, m, k = map(int, input().split())
board = [[None for _ in range(m)] for _ in range(n)]
new_board = [[[] for _ in range(m)] for _ in range(n)]
for _ in range(k):
    _x, _y, _s, _d, _b = map(int, input().split())
    board[_x - 1][_y - 1] = [_s, _d - 1, _b]

collect_score = 0


def in_range(x: int, y: int):
    return x in range(n) and y in range(m)


def collect(col: int):
    global collect_score
    for x in range(n):
        if not board[x][col]: continue
        collect_score += board[x][col][2]
        board[x][col] = None
        break


def move_mold():
    for x in range(n):
        for y in range(m):
            new_board[x][y].clear()

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    for x in range(n):
        for y in range(m):
            if not board[x][y]: continue
            s, d, b = board[x][y]
            # 상하
            if d in [0, 1]:
                tmp = x + (dx[d] * s)
                if abs(tmp // (n - 1)) % 2 == 0:
                    # 방향은 그대로
                    new_x = tmp % (n - 1)
                    new_board[new_x][y].append([s, d, b])
                else:
                    new_d = 0 if d == 1 else 1
                    new_x = (n - 1) - tmp % (n - 1)
                    new_board[new_x][y].append([s, new_d, b])
            # 좌우
            else:
                tmp = y + (dy[d] * s)
                if abs(tmp // (m - 1)) % 2 == 0:
                    # 방향은 그대로
                    new_y = tmp % (m - 1)
                    new_board[x][new_y].append([s, d, b])
                else:
                    new_d = 2 if d == 3 else 3
                    new_y = (m - 1) - tmp % (m - 1)
                    new_board[x][new_y].append([s, new_d, b])


def combine_mold():
    for x in range(n):
        for y in range(m):
            board[x][y] = None
            if not new_board[x][y]: continue
            if len(new_board) == 1:
                board[x][y] = new_board[x][y][0]
                continue
            # 최고 크기
            max_mold = sorted(new_board[x][y], key=lambda q: q[2], reverse=True)[0]
            board[x][y] = max_mold


if __name__ == '__main__':
    for _col in range(m):
        collect(col=_col)
        move_mold()
        combine_mold()

    print(collect_score)
