from collections import deque

n, m, q = map(int, input().split())
plate = []
for _ in range(n):
    plate.append(list(map(int, input().split())))
EMPTY = 0


def rotate_plate(x: int, d: int, k: int):
    for e in range(x, n + 1, x):
        r_x = e - 1
        origin = plate[r_x]
        for _ in range(k):
            # 시계
            if d == 0:
                origin = [origin[-1]] + origin[:-1]
            else:
                origin = origin[1:] + [origin[0]]
        plate[r_x] = origin


def delete_adjacency():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    is_removed = False
    for x in range(n):
        for y in range(m):
            if plate[x][y] == EMPTY: continue
            queue = deque()
            queue.append([x, y, plate[x][y]])

            while queue:
                cx, cy, number = queue.popleft()
                for i in range(4):
                    nx = cx + dx[i]
                    ny = (cy + dy[i]) % m
                    if nx not in range(n) or ny not in range(m): continue
                    if plate[nx][ny] != number: continue
                    queue.append([nx, ny, number])
                    plate[nx][ny] = EMPTY
                    is_removed = True
    if not is_removed:
        normalize()


# 정규화
def normalize():
    count = 0
    sum_number = 0
    for i in range(n):
        for j in range(m):
            if plate[i][j] == EMPTY: continue
            count += 1
            sum_number += plate[i][j]
    avg_number = sum_number // count
    for i in range(n):
        for j in range(m):
            if plate[i][j] == EMPTY: continue
            if plate[i][j] > avg_number:
                plate[i][j] -= 1
            elif plate[i][j] < avg_number:
                plate[i][j] += 1


def print_info():
    for row in plate:
        print(row)
    print("---------------------------------")


if __name__ == '__main__':
    for _ in range(q):
        _x, _d, _k = map(int, input().split())
        rotate_plate(x=_x, d=_d, k=_k)
        delete_adjacency()
    print(sum(sum(plate, [])))
