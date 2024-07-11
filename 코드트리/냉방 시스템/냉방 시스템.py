from collections import deque

n, m, k = map(int, input().split())

field = [[0 for _ in range(n)] for _ in range(n)]
air_conditioner_field = [[0 for _ in range(n)] for _ in range(n)]

left_wall = [[False for _ in range(n)] for _ in range(n)]
up_wall = [[False for _ in range(n)] for _ in range(n)]
right_wall = [[False for _ in range(n)] for _ in range(n)]
down_wall = [[False for _ in range(n)] for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

office_pos = []
air_conditioner_pos = []
wall_pos = []


def return_wall(direction: int):
    if direction == 0:
        return left_wall
    if direction == 1:
        return up_wall
    if direction == 2:
        return right_wall
    if direction == 3:
        return down_wall


def in_range(x, y):
    return x in range(n) and y in range(n)


def init_wall():
    for (x, y, s) in wall_pos:
        if s == 1:
            left_wall[x][y] = True
            right_wall[x][y - 1] = True
        else:
            up_wall[x][y] = True
            down_wall[x - 1][y] = True


def init_air_conditioner():
    for (_x, _y, _direction) in air_conditioner_pos:
        tmp_air_field = [[0 for _ in range(n)] for _ in range(n)]
        _nx = _x + dx[_direction]
        _ny = _y + dy[_direction]
        queue = deque()
        queue.append([_nx, _ny, _direction, 5])
        while queue:
            x, y, direction, power = queue.popleft()
            if power == 0: continue
            tmp_air_field[x][y] = power

            # 직진 먼저 고려
            nx = x + dx[direction]
            ny = y + dy[direction]
            if not in_range(nx, ny): continue
            wall = return_wall(direction)
            if not wall[x][y]:
                queue.append([nx, ny, direction, power - 1])

            # 위, 아래 체크
            if direction % 2 == 0:
                up_x = x + dx[1]
                up_y = y + dy[1]
                down_x = x + dx[3]
                down_y = y + dy[3]

                if in_range(up_x, up_y):
                    if direction == 0:
                        if not left_wall[up_x][up_y] and not down_wall[up_x][up_y]:
                            if in_range(up_x, up_y + dy[direction]):
                                queue.append([up_x, up_y + dy[direction], direction, power - 1])
                    else:
                        if not right_wall[up_x][up_y] and not down_wall[up_x][up_y]:
                            if in_range(up_x, up_y + dy[direction]):
                                queue.append([up_x, up_y + dy[direction], direction, power - 1])

                if in_range(down_x, down_y):
                    if direction == 0:
                        if not left_wall[down_x][down_y] and not up_wall[down_x][down_y]:
                            if in_range(down_x, down_y + dy[direction]):
                                queue.append([down_x, down_y + dy[direction], direction, power - 1])
                    else:
                        if not right_wall[down_x][down_y] and not up_wall[down_x][down_y]:
                            if in_range(down_x, down_y + dy[direction]):
                                queue.append([down_x, down_y + dy[direction], direction, power - 1])
            # 왼, 오
            else:
                left_x = x + dx[0]
                left_y = y + dy[0]
                right_x = x + dx[2]
                right_y = y + dy[2]

                if in_range(left_x, left_y):
                    if direction == 1:
                        if not right_wall[left_x][left_y] and not up_wall[left_x][left_y]:
                            if in_range(left_x + dx[direction], left_y):
                                queue.append([left_x + dx[direction], left_y, direction, power - 1])
                    else:
                        if not right_wall[left_x][left_y] and not down_wall[left_x][left_y]:
                            if in_range(left_x + dx[direction], left_y):
                                queue.append([left_x + dx[direction], left_y, direction, power - 1])

                if in_range(right_x, right_y):
                    if direction == 1:
                        if not left_wall[right_x][right_y] and not up_wall[right_x][right_y]:
                            if in_range(right_x + dx[direction], right_y):
                                queue.append([right_x + dx[direction], right_y, direction, power - 1])
                    else:
                        if not left_wall[right_x][right_y] and not down_wall[right_x][right_y]:
                            if in_range(right_x + dx[direction], right_y):
                                queue.append([right_x + dx[direction], right_y, direction, power - 1])

        for i in range(n):
            for j in range(n):
                air_conditioner_field[i][j] += tmp_air_field[i][j]


def operate():
    for i in range(n):
        for j in range(n):
            field[i][j] += air_conditioner_field[i][j]

    visited = [[False for _ in range(n)] for _ in range(n)]
    tmp = [[0 for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not in_range(nx, ny): continue
                if visited[nx][ny]: continue
                wall = return_wall(direction=i)
                if wall[x][y]: continue

                diff = abs(field[x][y] - field[nx][ny]) // 4
                if field[x][y] > field[nx][ny]:
                    tmp[x][y] -= diff
                    tmp[nx][ny] += diff
                else:
                    tmp[x][y] += diff
                    tmp[nx][ny] -= diff

    for x in range(n):
        for y in range(n):
            field[x][y] += tmp[x][y]

    for x in range(n):
        for y in range(n):
            if x in [0, n - 1] or y in [0, n - 1]:
                field[x][y] = max(field[x][y] - 1, 0)


def check_end():
    for x, y in office_pos:
        if field[x][y] < k:
            return False
    return True


if __name__ == '__main__':
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(n):
            if row[j] == 1:
                office_pos.append([i, j])
            if row[j] > 1:
                air_conditioner_pos.append([i, j, row[j] - 2])

    for _ in range(m):
        inputs = list(map(int, input().split()))
        wall_pos.append([inputs[0] - 1, inputs[1] - 1, inputs[2]])

    init_wall()
    init_air_conditioner()

    time = 0

    while time <= 100:
        time += 1
        operate()

        if check_end():
            break

    print(time if time <= 100 else -1)
