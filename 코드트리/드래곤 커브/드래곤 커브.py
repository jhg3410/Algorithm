n = int(input())
board = [[False for _ in range(100)] for _ in range(100)]
dxs = [0, -1, 0, 1]
dys = [1, 0, -1, 0]


def draw(x: int, y: int, d: int, g: int):
    nx = x + dxs[d]
    ny = y + dys[d]
    board[x][y] = True
    board[nx][ny] = True
    last_x = nx
    last_y = ny
    directions = [d]

    for _ in range(g):
        new_directions = []
        for direction in directions[::-1]:
            r_d = (direction + 1) % 4
            new_directions.append(r_d)
            new_x, new_y = last_x + dxs[r_d], last_y + dys[r_d]
            board[last_x][last_y] = True
            board[new_x][new_y] = True
            last_x, last_y = new_x, new_y

        directions += new_directions


def get_rect_count():
    count = 0
    for x in range(99):
        for y in range(99):
            is_rect = True
            for i in range(2):
                for j in range(2):
                    if not board[x + i][y + j]:
                        is_rect = False

            if is_rect: count += 1

    return count


if __name__ == '__main__':
    for _ in range(n):
        _x, _y, _d, _g = map(int, input().split())
        draw(x=_x, y=_y, d=_d, g=_g)
    print(get_rect_count())
