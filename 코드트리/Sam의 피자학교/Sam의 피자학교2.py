n, k = map(int, input().split())
dow = list(map(int, input().split()))
rolled_dow = []


def put_flour():
    min_flour = min(dow)
    for idx, flour in enumerate(dow):
        if flour == min_flour:
            dow[idx] += 1


def roll_dow():
    global dow, rolled_dow
    rolled_dow.append([dow.pop(0)])
    while True:
        width_rolled_dow = len(rolled_dow[0])

        rolled_dow.append(dow[:width_rolled_dow])
        dow = dow[width_rolled_dow:]
        if len(rolled_dow) > len(dow): break
        rolled_dow = rotate(rolled_dow)

    rolled_dow[-1].extend(dow[:])
    fill_zero(rolled_dow)


def rotate(r_dow: list[list[int]]):
    max_n = max(len(r_dow), len(r_dow[0]))
    fill_zero(r_dow)
    new_dow = [[0 for _ in range(max_n)] for _ in range(max_n)]

    # 회전
    for x in range(max_n):
        for y in range(max_n):
            new_dow[x][y] = r_dow[max_n - 1 - y][x]

    # 다시 0 제거
    for idx, row in enumerate(new_dow):
        new_dow[idx] = list(filter(lambda x: x > 0, row))
    new_dow = list(filter(lambda x: len(x) > 0, new_dow))

    return new_dow


def fill_zero(r_dow):
    max_n = max(len(r_dow), max(list(map(lambda x: len(x), r_dow))))

    # 가로 채우기
    for row in r_dow:
        row.extend([0 for _ in range(max_n - len(row))])

    # 세로 채우기
    for _ in range(max_n - len(r_dow)):
        r_dow.append([0 for _ in range(max_n)])


def press_dow():
    global rolled_dow
    dow.clear()
    fill_zero(rolled_dow)
    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
    r_n = len(rolled_dow)
    pressed_dow = [[0 for _ in range(r_n)] for _ in range(r_n)]

    for x in range(r_n):
        for y in range(r_n):
            a = rolled_dow[x][y]
            if a == 0: continue
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if nx not in range(r_n) or ny not in range(r_n): continue
                b = rolled_dow[nx][ny]
                if b == 0: continue
                d = abs(a - b) // 5
                if a < b:
                    pressed_dow[x][y] += d
                    pressed_dow[nx][ny] -= d
                else:
                    pressed_dow[nx][ny] += d
                    pressed_dow[x][y] -= d

    for x in range(r_n):
        for y in range(r_n):
            rolled_dow[x][y] += pressed_dow[x][y] // 2

    # 도우 일자로 피기
    for y in range(r_n):
        for x in range(r_n - 1, -1, -1):
            if rolled_dow[x][y] != 0:
                dow.append(rolled_dow[x][y])

    rolled_dow.clear()


def roll_dow_twice():
    rolled_dow.append(dow[:n // 2][::-1])
    rolled_dow.append(dow[n // 2:])
    tmp_dow = []
    for idx, row in enumerate(rolled_dow):
        tmp_dow.append(row[:len(row) // 2])
        rolled_dow[idx] = row[len(row) // 2:]

    for row in reversed(rotate(rotate(tmp_dow))):
        rolled_dow.insert(0, row)


if __name__ == '__main__':
    turn = 0
    while max(dow) - min(dow) > k:
        turn += 1
        put_flour()
        roll_dow()
        press_dow()
        roll_dow_twice()
        press_dow()
    print(turn)
