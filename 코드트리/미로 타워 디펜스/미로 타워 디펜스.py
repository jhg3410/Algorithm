total_score = 0
board = []
top = []

attack_dx = [0, 1, 0, -1]
attack_dy = [1, 0, -1, 0]

board_dx = [0, 1, 0, -1]
board_dy = [-1, 0, 1, 0]


def in_range(x: int, y: int):
    return x in range(n) and y in range(n)


def start_game(direction: int, p: int):
    global total_score

    attack(direction=direction, p=p)

    while True:
        surviving_monsters = get_monsters()
        set_monsters(surviving_monsters)
        score = delete()
        if score == 0:
            break
        total_score += score

    surviving_monsters = get_monsters()
    transferred_monsters = transfer_monsters(monsters=surviving_monsters)
    set_monsters(transferred_monsters)


def attack(direction: int, p: int):
    global total_score
    top_x = top[0]
    top_y = top[1]

    nx = top_x
    ny = top_y
    for _ in range(p):
        nx += attack_dx[direction]
        ny += attack_dy[direction]
        total_score += board[nx][ny]
        board[nx][ny] = 0


def get_monsters():
    new_monsters = []
    miro_direction = 0
    now_x = top[0]
    now_y = top[1]

    for offset in range(1, n):
        for _ in range(offset):
            now_x += board_dx[miro_direction]
            now_y += board_dy[miro_direction]
            if board[now_x][now_y] != 0:
                new_monsters.append(board[now_x][now_y])
        miro_direction = (miro_direction + 1) % 4
        for _ in range(offset):
            now_x += board_dx[miro_direction]
            now_y += board_dy[miro_direction]
            if board[now_x][now_y] != 0:
                new_monsters.append(board[now_x][now_y])
        miro_direction = (miro_direction + 1) % 4

    for _ in range(n-1):
        now_x += board_dx[miro_direction]
        now_y += board_dy[miro_direction]
        if board[now_x][now_y] != 0:
            new_monsters.append(board[now_x][now_y])

    return new_monsters


def set_monsters(monsters: list[int]):
    for i in range(n):
        for j in range(n):
            board[i][j] = 0

    miro_direction = 0
    now_x = top[0]
    now_y = top[1]

    for offset in range(1, n):
        for _ in range(offset):
            now_x += board_dx[miro_direction]
            now_y += board_dy[miro_direction]
            if monsters:
                board[now_x][now_y] = monsters.pop(0)
        miro_direction = (miro_direction + 1) % 4
        for _ in range(offset):
            now_x += board_dx[miro_direction]
            now_y += board_dy[miro_direction]
            if monsters:
                board[now_x][now_y] = monsters.pop(0)
        miro_direction = (miro_direction + 1) % 4

    for _ in range(n-1):
        now_x += board_dx[miro_direction]
        now_y += board_dy[miro_direction]
        if monsters:
            board[now_x][now_y] = monsters.pop(0)


def delete():
    score = 0
    monsters = get_monsters()
    deleted_monsters = []
    count = 0
    number = 0
    for monster in monsters:
        if monster != number:
            if count < 4:
                for _ in range(count):
                    deleted_monsters.append(number)
            else:
                score += number * count
            count = 1
            number = monster
        else:
            count += 1

    if count < 4:
        for _ in range(count):
            deleted_monsters.append(number)
    else:
        score += number * count

    if score != 0:
        set_monsters(monsters=deleted_monsters)
    return score


def transfer_monsters(monsters: list[int]):
    transferred = []
    stack = []

    for idx, monster in enumerate(monsters):
        if not stack:
            stack.append(monster)
            continue

        if stack[-1] == monster:
            stack.append(monster)
        else:
            transferred.extend([len(stack), stack[-1]])
            stack.clear()
            stack.append(monster)

    transferred.extend([len(stack), stack[-1]])

    return transferred


if __name__ == '__main__':
    n, m = map(int, input().split())
    top = [n // 2, n // 2]
    for _ in range(n):
        inputs = list(map(int, input().split()))
        board.append(inputs)

    for _ in range(m):
        d, _p = map(int, input().split())
        start_game(direction=d, p=_p)

    print(total_score)
