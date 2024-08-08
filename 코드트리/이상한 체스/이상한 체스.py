n, m = map(int, input().split())
selected = []
board = [list(map(int, input().split())) for _ in range(n)]
my_piece_count = 0
for i in range(n):
    for j in range(m):
        if board[i][j] in range(1, 6):
            my_piece_count += 1

visited = [[False for _ in range(m)] for _ in range(n)]
answer = 10 ** 6

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def get_routes(piece_type: int, piece_dir: int):
    if piece_type == 1:
        return [piece_dir, (piece_dir + 2) % 4]
    elif piece_type == 2:
        return [piece_dir, (piece_dir + 1) % 4]
    elif piece_type == 3:
        return [piece_dir, (piece_dir - 1) % 4, (piece_dir + 1) % 4]
    else:
        return [0, 1, 2, 3]


def in_range(x: int, y: int):
    return x in range(n) and y in range(m)


def init():
    for x in range(n):
        for y in range(m):
            visited[x][y] = False


def find_all_case_type():
    global answer
    global selected
    if len(selected) == my_piece_count:
        answer = min(answer, get_empty_count())
        return

    for i in range(4):
        selected.append(i)
        find_all_case_type()
        selected.pop()


def get_empty_count():
    init()
    number = 0
    for x in range(n):
        for y in range(m):
            if board[x][y] in range(1, 6):
                visited[x][y] = True
                piece_type = board[x][y]
                piece_dir = selected[number]
                number += 1
                routes = get_routes(piece_type=piece_type - 1, piece_dir=piece_dir)
                for route in routes:
                    nx, ny = x, y
                    while True:
                        next_nx, next_ny = nx + dx[route], ny + dy[route]
                        if not in_range(next_nx, next_ny): break
                        if board[next_nx][next_ny] == 6: break
                        nx, ny = next_nx, next_ny
                        visited[next_nx][next_ny] = True
    count = 0
    for x in range(n):
        for y in range(m):
            if not visited[x][y] and board[x][y] != 6:
                count += 1

    return count


if __name__ == '__main__':
    find_all_case_type()
    print(answer)
