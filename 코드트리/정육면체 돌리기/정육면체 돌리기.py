dice = [0, 0, 0, 0, 0, 0]

n, m, dice_x, dice_y, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(lambda x: int(x) - 1, input().split()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice_rotate_helper = [
    # 동쪽
    [5, 1, 4, 3, 0, 2],
    # 서쪽
    [4, 1, 5, 3, 2, 0],
    # 북쪽
    [3, 0, 1, 2, 4, 5],
    # 남쪽
    [1, 2, 3, 0, 4, 5]
]


def in_range(x: int, y: int):
    return x in range(n) and y in range(m)


def game_start():
    for command in commands:
        rotate_dice(direction=command)


def rotate_dice(direction: int):
    global dice, dice_x, dice_y

    nx = dice_x + dx[direction]
    ny = dice_y + dy[direction]
    if not in_range(nx, ny): return

    new_dice = [0 for _ in range(6)]
    for idx in range(6):
        new_dice[idx] = dice[dice_rotate_helper[direction][idx]]

    dice = new_dice
    dice_x, dice_y = nx, ny

    down = dice[0]
    board_dice = board[dice_x][dice_y]

    if board_dice == 0:
        board[dice_x][dice_y] = down
    else:
        dice[0] = board_dice
        board[dice_x][dice_y] = 0

    print(dice[2])


if __name__ == '__main__':
    game_start()
