dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
direction = "dlru"
n, m = 0, 0


def check_out(x, y):
    return x in range(n) and y in range(m)


def get_distance(ax, ay, bx, by):
    return abs(ax - bx) + abs(ay - by)


def solution(_n, _m, _x, _y, r, c, k):
    global n, m
    n, m = _n, _m

    result = ""
    x, y = _x - 1, _y - 1
    e_x, e_y = r - 1, c - 1

    distance = get_distance(x, y, e_x, e_y)
    diff = k - distance
    if diff < 0 or diff % 2 != 0: return "impossible"

    while k != 0 or x != e_x or y != e_y:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not check_out(nx, ny): continue
            distance = get_distance(nx, ny, e_x, e_y)
            diff = k - 1 - distance
            if diff < 0 or diff % 2 != 0: continue
            x, y = nx, ny
            result += direction[i]
            k -= 1
            break

    return result


if __name__ == '__main__':
    solution(3, 4, 2, 3, 3, 1, 5)
