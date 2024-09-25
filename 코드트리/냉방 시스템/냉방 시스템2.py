# 1시간 41분

from collections import deque

# 상, 우, 하, 좌
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

# 0 - 왼쪽 방향, 1 - 위쪽 방향, 2 - 오른쪽 방향, 3- 아래 방향
air_direction = [
    [[3], [0, 3], [2, 3]],
    [[0], [3, 0], [1, 0]],
    [[1], [0, 1], [2, 1]],
    [[2], [3, 2], [1, 2]]
]

air_conditioner = []
office = []

n, m, k = map(int, input().split())

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            office.append([i, j])
        if row[j] > 1:
            air_conditioner.append([i, j, row[j] - 2])

air = [[0 for _ in range(n)] for _ in range(n)]
# wall[x][y][dir]
# dir - 상, 우, 하, 좌
wall = [[[False for _ in range(4)] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    wx, wy, wd = map(int, input().split())
    wx -= 1
    wy -= 1
    if wd == 0:
        wall[wx][wy][0] = True
        wall[wx - 1][wy][2] = True
    else:
        wall[wx][wy][3] = True
        wall[wx][wy - 1][1] = True


def in_range(x: int, y: int):
    return x in range(n) and y in range(n)


# 에어컨 동작
def operate_air_conditioner():
    for x, y, direction in air_conditioner:
        visited = [[False for _ in range(n)] for _ in range(n)]
        air_d = air_direction[direction]
        queue = deque()
        queue.append([x + dxs[air_d[0][0]], y + dys[air_d[0][0]], 5])
        while queue:
            qx, qy, air_level = queue.popleft()
            air[qx][qy] += air_level
            if air_level == 1:
                continue
            for directions in air_d:
                nx, ny = qx, qy
                is_wall = False
                for d in directions:
                    if wall[nx][ny][d]:
                        is_wall = True
                        break
                    nx += dxs[d]
                    ny += dys[d]
                    if not in_range(nx, ny):
                        is_wall = True
                        break
                if not is_wall and not visited[nx][ny]:
                    queue.append([nx, ny, air_level - 1])
                    visited[nx][ny] = True


# 공기 섞임
def mix_air():
    offsets = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            air_level = air[x][y]
            for idx in range(4):
                nx = x + dxs[idx]
                ny = y + dys[idx]
                if not in_range(nx, ny): continue
                # 벽이 있다면 안 섞인다.
                if wall[x][y][idx]: continue
                new_air_level = air[nx][ny]
                diff = abs(air_level - new_air_level) // 4
                if air_level > new_air_level:
                    offsets[x][y] -= diff
                    offsets[nx][ny] += diff
                else:
                    offsets[x][y] += diff
                    offsets[nx][ny] -= diff

    for x in range(n):
        for y in range(n):
            air[x][y] += (offsets[x][y]) // 2


# 외벽은 1씩 감소
def decrease_wall():
    for x in range(n):
        for y in range(n):
            if x == 0 or y == 0 or x == n - 1 or y == n - 1:
                air[x][y] = max(air[x][y] - 1, 0)


# 끝나는지 확안
def is_end():
    for x, y in office:
        if air[x][y] < k:
            return False
    return True


if __name__ == '__main__':
    time = 0

    while not is_end():
        operate_air_conditioner()

        mix_air()
        decrease_wall()
        time += 1
        if time > 100:
            time = -1
            break

    print(time)
