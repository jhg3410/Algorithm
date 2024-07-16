board = []
n = int(input())
for _ in range(n):
    board.append(list(map(int, input().split())))

percent = [5, 10, 10, 7, 7, 1, 1, 2, 2]
# 왼, 아래, 오, 위
percent_dx = [[0, -1, 1, -1, 1, -1, 1, -2, 2],
              [2, 1, 1, 0, 0, -1, -1, 0, 0],
              [0, -1, 1, 1, -1, -1, 1, 2, -2],
              [-2, -1, -1, 0, 0, 1, 1, 0, 0]]
percent_dy = [[-2, -1, -1, 0, 0, 1, 1, 0, 0],
              [0, -1, 1, 1, -1, -1, 1, 2, -2],
              [2, 1, 1, 0, 0, -1, -1, 0, 0],
              [0, 1, -1, 1, -1, 1, -1, 2, -2]]

# 왼, 아래, 오, 위
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

stick_x = stick_y = n // 2
stick_direction = 0  # 왼

score = 0


def in_range(x: int, y: int):
    return x in range(n) and y in range(n)


def start():
    move()


def move():
    global stick_x, stick_y, stick_direction

    for dist in range(1, n):
        for j in range(2):
            for k in range(dist):
                stick_x += dx[stick_direction]
                stick_y += dy[stick_direction]
                sweep()
            stick_direction = (stick_direction + 1) % 4

    for _ in range(n - 1):
        stick_x += dx[stick_direction]
        stick_y += dy[stick_direction]
        sweep()


def sweep():
    global score

    current_dust = board[stick_x][stick_y]
    remain_dust = current_dust
    board[stick_x][stick_y] = 0

    for i in range(len(percent)):
        p_x = stick_x + percent_dx[stick_direction][i]
        p_y = stick_y + percent_dy[stick_direction][i]
        send_dust = int(current_dust * (percent[i]/100))
        remain_dust -= send_dust

        if not in_range(p_x, p_y):
            score += send_dust
        else:
            board[p_x][p_y] += send_dust

    a_x = stick_x + dx[stick_direction]
    a_y = stick_y + dy[stick_direction]

    if not in_range(a_x, a_y):
        score += remain_dust
    else:
        board[a_x][a_y] += remain_dust


if __name__ == '__main__':
    start()
    print(score)
