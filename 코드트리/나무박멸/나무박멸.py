n, m, k, c = map(int, input().split())
trees = [list(map(int, input().split())) for _ in range(n)]
killers = [[0 for _ in range(n)] for _ in range(n)]

kill_tree_count = 0


def in_range(x: int, y: int):
    return x in range(n) and y in range(n)


def grow_tree():
    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
    tmp = [[0 for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if trees[x][y] <= 0: continue
            count = 0
            for dx, dy in zip(dxs, dys):
                nx = x + dx
                ny = y + dy
                if not in_range(nx, ny) or trees[nx][ny] <= 0: continue
                count += 1
            tmp[x][y] += count

    for x in range(n):
        for y in range(n):
            trees[x][y] += tmp[x][y]


def breed_tree():
    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
    tmp = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            stored = []
            if trees[x][y] <= 0: continue
            for dx, dy in zip(dxs, dys):
                nx = x + dx
                ny = y + dy
                if not in_range(nx, ny) or trees[nx][ny] != 0 or killers[nx][ny] != 0: continue
                stored.append([nx, ny])
            for sx, sy in stored:
                tmp[sx][sy] += trees[x][y] // len(stored)

    for x in range(n):
        for y in range(n):
            trees[x][y] += tmp[x][y]


def inject_killer():
    global kill_tree_count
    dxs = [1, 1, -1, -1]
    dys = [1, -1, 1, -1]
    kill_count = -1
    killer_pos = []
    for x in range(n):
        for y in range(n):
            if trees[x][y] == -1: continue
            new_kill_count = cal_kill_count(x, y)
            if new_kill_count > kill_count:
                kill_count = new_kill_count
                killer_pos = [x, y]

    kill_tree_count += kill_count
    kx, ky = killer_pos
    trees[kx][ky] = 0
    killers[kx][ky] = c + 1

    for dx, dy in zip(dxs, dys):
        for i in range(1, k + 1):
            nx = kx + (dx * i)
            ny = ky + (dy * i)
            if not in_range(nx, ny): break
            if trees[nx][ny] <= 0:
                killers[nx][ny] = c + 1
                break
            else:
                killers[nx][ny] = c + 1
                trees[nx][ny] = 0


def cal_kill_count(x: int, y: int):
    if trees[x][y] == 0:
        return 0
    count = trees[x][y]
    dxs = [1, 1, -1, -1]
    dys = [1, -1, 1, -1]
    for dx, dy in zip(dxs, dys):
        for i in range(1, k + 1):
            nx = x + (dx * i)
            ny = y + (dy * i)
            if not in_range(nx, ny): break
            if trees[nx][ny] <= 0: break
            count += trees[nx][ny]

    return count


def decrease_killer():
    for x in range(n):
        for y in range(n):
            killers[x][y] = max(killers[x][y] - 1, 0)


if __name__ == '__main__':
    for _ in range(m):
        grow_tree()
        breed_tree()
        inject_killer()
        decrease_killer()

    print(kill_tree_count)
