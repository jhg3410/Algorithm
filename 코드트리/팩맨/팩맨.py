m, t = map(int, input().split())
packman = list(map(lambda x: int(x) - 1, input().split()))
monster_board = [[[] for _ in range(4)] for _ in range(4)]
eggs = []
died = [[[] for _ in range(4)] for _ in range(4)]

for _ in range(m):
    r, c, d = map(lambda x: int(x) - 1, input().split())
    monster_board[r][c].append(d)


def in_range(x: int, y: int):
    return x in range(4) and y in range(4)


def lay_eggs():
    for x in range(4):
        for y in range(4):
            for direction in monster_board[x][y]:
                eggs.append([x, y, direction])


def move_monster():
    dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]
    new_monster_board = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            for direction in monster_board[x][y]:
                nd = direction
                while True:
                    nx = x + dxs[nd]
                    ny = y + dys[nd]
                    if (not in_range(nx, ny)) or died[nx][ny] or (nx == packman[0] and ny == packman[1]):
                        nd = (nd + 1) % 8
                    else:
                        new_monster_board[nx][ny].append(nd)
                        break
                    if nd == direction:
                        new_monster_board[x][y].append(direction)
                        break
    for x in range(4):
        for y in range(4):
            monster_board[x][y] = new_monster_board[x][y]


dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]
most_eat_count = -1
best_direction = list()


def find_best_location_packman(directions: list[int], eat_count: int, current_pos: list[int]):
    global most_eat_count, best_direction
    if len(directions) == 3:
        if eat_count > most_eat_count:
            most_eat_count = eat_count
            best_direction = directions.copy()
        return

    for i in range(4):
        nx, ny = current_pos[0] + dxs[i], current_pos[1] + dys[i]
        if not in_range(nx, ny): continue
        directions.append(i)
        stored = []
        for direction in monster_board[nx][ny]:
            stored.append(direction)
        new_eat_count = eat_count + len(monster_board[nx][ny])
        monster_board[nx][ny].clear()
        find_best_location_packman(directions=directions, eat_count=new_eat_count,
                                   current_pos=[nx, ny])
        for direction in stored:
            monster_board[nx][ny].append(direction)
        directions.pop()


def move_packman():
    global packman, most_eat_count
    find_best_location_packman([], 0, packman)
    most_eat_count = 0
    for direction in best_direction:
        packman[0] += dxs[direction]
        packman[1] += dys[direction]
        p_x = packman[0]
        p_y = packman[1]
        for _ in range(len(monster_board[p_x][p_y])):
            died[p_x][p_y].append(3)

        monster_board[p_x][p_y].clear()


def delete_died():
    for x in range(4):
        for y in range(4):
            died[x][y] = list(filter(lambda x: x > 0, (map(lambda x: x - 1, died[x][y]))))


def duplicate():
    for x, y, direction in eggs:
        monster_board[x][y].append(direction)
    eggs.clear()


if __name__ == '__main__':
    for _ in range(t):
        lay_eggs()
        move_monster()
        move_packman()
        delete_died()
        duplicate()

    print(sum([len(monster_board[i][j]) for i in range(4) for j in range(4)]))