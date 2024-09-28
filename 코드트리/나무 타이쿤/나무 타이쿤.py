n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
move_rule = []
for _ in range(m):
    _d, _p = map(int, input().split())
    move_rule.append((_d - 1, _p))
# 영양제 위치
medicines = set()
medicines.add((n - 2, 0))
medicines.add((n - 2, 1))
medicines.add((n - 1, 0))
medicines.add((n - 1, 1))
dxs = [0, -1, -1, -1, 0, 1, 1, 1]
dys = [1, 1, 0, -1, -1, -1, 0, 1]


def in_range(x: int, y: int):
    return x in range(n) and y in range(n)


def move_medicine():
    global medicines
    # 이동 방향, 칸 수
    d, p = move_rule.pop(0)
    new_medicines = set()
    for x, y in medicines:
        nx = (x + (p * dxs[d])) % n
        ny = (y + (p * dys[d])) % n
        new_medicines.add((nx, ny))

    medicines = new_medicines


def inject_medicine():
    for x, y in medicines:
        board[x][y] += 1


def extra_grow_tree():
    for x, y in medicines:
        count = 0
        for dx, dy in zip(dxs[1::2], dys[1::2]):
            nx = x + dx
            ny = y + dy
            if not in_range(nx, ny): continue
            if board[nx][ny] > 0:
                count += 1
        board[x][y] += count


def buy_medicine():
    global medicines

    new_medicines = set()
    for x in range(n):
        for y in range(n):
            if (x, y) in medicines or board[x][y] < 2: continue
            board[x][y] -= 2
            new_medicines.add((x, y))

    medicines = new_medicines


if __name__ == '__main__':
    for _ in range(m):
        move_medicine()
        inject_medicine()
        extra_grow_tree()
        buy_medicine()

    print(sum([board[ai][aj] for ai in range(n) for aj in range(n)]))
