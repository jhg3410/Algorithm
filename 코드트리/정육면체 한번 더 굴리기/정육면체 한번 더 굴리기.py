# 1시간 9분

from collections import deque

dice = [1, 2, 6, 5, 3, 4]
dice_x = 0
dice_y = 0
dice_dir = 1
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
score = 0


def in_range(x: int, y: int):
    return x in range(n) and y in range(n)


# direction: 0 - 위, 1 - 오른, 2 - 아래, 3 - 왼
def move_dice():
    global dice, dice_x, dice_y, dice_dir

    nx, ny = dice_x + dxs[dice_dir], dice_y + dys[dice_dir]
    if not in_range(nx, ny):
        dice_dir = (dice_dir + 2) % 4
    dice_x, dice_y = dice_x + dxs[dice_dir], dice_y + dys[dice_dir]
    if dice_dir == 0:
        new_dice = dice[1:4] + [dice[0]] + dice[4:6]
    elif dice_dir == 1:
        new_dice = [dice[5]] + [dice[1]] + [dice[4]] + [dice[3]] + [dice[0]] + [dice[2]]
    elif dice_dir == 2:
        new_dice = [dice[3]] + dice[0:3] + dice[4:6]
    else:
        new_dice = [dice[4]] + [dice[1]] + [dice[5]] + [dice[3]] + [dice[2]] + [dice[0]]

    dice = new_dice


def get_score():
    global score
    x, y = dice_x, dice_y
    number = board[x][y]
    queue = deque()
    queue.append([x, y])
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[x][y] = True

    while queue:
        qx, qy = queue.popleft()
        score += number
        for dx, dy in zip(dxs, dys):
            nx = qx + dx
            ny = qy + dy
            if nx not in range(n) or ny not in range(n): continue
            if visited[nx][ny] or board[nx][ny] != number: continue
            queue.append([nx, ny])
            visited[nx][ny] = True


def change_direction():
    global dice_dir
    bottom = dice[2]
    number = board[dice_x][dice_y]
    if bottom > number:
        dice_dir = (dice_dir + 1) % 4
    elif bottom < number:
        dice_dir = (dice_dir - 1) % 4


if __name__ == '__main__':
    for _ in range(m):
        move_dice()
        get_score()
        change_direction()

    print(score)
