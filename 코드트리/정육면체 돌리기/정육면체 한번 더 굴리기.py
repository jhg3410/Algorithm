from collections import deque

dice = [1, 2, 6, 5, 3, 4]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
score = 0


# direction: 0 - 위, 1 - 오른, 2 - 아래, 3 - 왼
def move_dice(direction: int):
    global dice
    if direction == 0:
        new_dice = dice[1:4] + [dice[0]] + dice[4:6]
    elif direction == 1:
        new_dice = [dice[4]] + [dice[1]] + [dice[5]] + [dice[3]] + [dice[0]] + [dice[2]]
    elif direction == 2:
        new_dice = [dice[3]] + list(reversed(dice[0:3])) + dice[4:6]
    else:
        new_dice = [dice[4]] + [dice[1]] + [dice[5]] + [dice[3]] + [dice[2]] + [dice[0]]

    dice = new_dice


def get_score(x: int, y: int):
    global score
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

