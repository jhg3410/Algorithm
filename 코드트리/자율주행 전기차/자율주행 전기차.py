from collections import deque
import heapq

n, m, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
mans = [[[] for _ in range(n)] for _ in range(n)]
destinations = dict()
taxi_pos = list(map(lambda x: int(x) - 1, input().split()))
for number in range(m):
    m_x, m_y, d_x, d_y = map(lambda x: int(x) - 1, input().split())
    mans[m_x][m_y].append(number + 1)
    destinations[number + 1] = [d_x, d_y]
power = c

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def is_in(x: int, y: int):
    return x in range(n) and y in range(n)


def print_info():
    print(f'power = {power}')
    print(f'taxi_pos = {taxi_pos}')
    print("------------")


def drive_taxi():
    global power
    while not is_end():
        man = pick_up()
        if man == -1:
            power = -1
            break
        dist = drop_off(man=man)
        power -= dist
        if power < 0:
            power = -1
            break
        power += dist * 2

    print(power)


def pick_up():
    global taxi_pos, power
    queue = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue.append([taxi_pos, 0])
    visited[taxi_pos[0]][taxi_pos[1]] = True
    find_mans = []

    while queue:
        (x, y), dist = queue.popleft()
        if mans[x][y]:
            heapq.heappush(find_mans, [dist, x, y, mans[x][y][0]])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not is_in(nx, ny): continue
            if board[nx][ny] == 1: continue
            if visited[nx][ny]: continue
            queue.append([[nx, ny], dist + 1])
            visited[nx][ny] = True

    if not find_mans:
        return -1
    find_man = heapq.heappop(find_mans)
    f_dist, f_x, f_y, f_number = find_man
    mans[f_x][f_y].remove(f_number)
    taxi_pos = [f_x, f_y]
    power -= f_dist

    if power < 0:
        return -1
    return f_number


def drop_off(man: int):
    global taxi_pos, power
    dist = 0
    destination_pos = destinations[man]
    queue = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue.append([taxi_pos, 0])
    visited[taxi_pos[0]][taxi_pos[1]] = True

    while queue:
        (x, y), local_dist = queue.popleft()
        if x == destination_pos[0] and y == destination_pos[1]:
            taxi_pos = [x, y]
            dist = local_dist
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not is_in(nx, ny): continue
            if board[nx][ny] == 1: continue
            if visited[nx][ny]: continue
            queue.append([[nx, ny], local_dist + 1])
            visited[nx][ny] = True

    destinations.pop(man)
    return dist


def is_end():
    return not destinations


if __name__ == '__main__':
    drive_taxi()
