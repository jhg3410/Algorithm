n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
tmp_board = [[0 for _ in range(n)] for _ in range(n)]
rotate_tmp_board = [[0 for _ in range(n)] for _ in range(n)]
answer = 0


def get_5_case(dirs: list[int]):
    if len(dirs) == 5:
        start_game(directions=dirs)
        return

    for i in range(4):
        dirs.append(i)
        get_5_case(dirs=dirs)
        dirs.pop()


def start_game(directions: list[int]):
    global answer
    for x in range(n):
        for y in range(n):
            tmp_board[x][y] = board[x][y]

    for direction in directions:
        for _ in range(direction):
            rotate()
        merge()
        for _ in range(4 - direction):
            rotate()

    answer = max(answer, max([
        tmp_board[x][y]
        for x in range(n)
        for y in range(n)
    ]))


# 오른쪽 시계방향 회전
def rotate():
    for x in range(n):
        for y in range(n):
            rotate_tmp_board[x][y] = tmp_board[n - 1 - y][x]

    for x in range(n):
        for y in range(n):
            tmp_board[x][y] = rotate_tmp_board[x][y]


# 아래로만
def merge():
    merged = [[False for _ in range(n)] for _ in range(n)]

    for y in range(n):
        for x in range(n - 1, -1, -1):
            if tmp_board[x][y] == 0: continue
            number = tmp_board[x][y]
            tmp_board[x][y] = 0
            nx, ny = x, y
            while True:
                # 범위 벗어나면
                if nx + 1 not in range(n) or ny not in range(n): break
                # 다음 칸이 빈 칸이면
                if tmp_board[nx + 1][ny] == 0:
                    nx += 1
                    continue
                # 다음 칸이 나랑 같지 않으면 그만
                if tmp_board[nx + 1][ny] != number: break
                # 다음 칸이 나랑 같고, 변한 적이 없으면
                if tmp_board[nx + 1][ny] == number:
                    if not merged[nx + 1][ny]:
                        number *= 2
                        merged[nx + 1][ny] = True
                        nx += 1
                        break
                    else:
                        break
            tmp_board[nx][ny] = number


if __name__ == '__main__':
    get_5_case([])
    print(answer)
