import heapq
from collections import deque

n = int(input())
board = []
robot_pos = []
for _x in range(n):
    row = list(map(int, input().split()))
    for _y in range(n):
        if row[_y] == 9:
            robot_pos = [_x, _y]
    board.append(row)
board[robot_pos[0]][robot_pos[1]] = 0
robot_level = 2
robot_stack = 0
time = 0


def can_go(x: int, y: int):
    if x not in range(n) or y not in range(n): return False
    if board[x][y] > robot_level: return False
    return True


def find_food():
    global robot_pos, time
    dxs = [-1, 0, 0, 1]
    dys = [0, -1, 1, 0]
    queue = deque()
    queue.append([robot_pos, 0])
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[robot_pos[0]][robot_pos[1]] = True
    poses = []

    while queue:
        (x, y), count = queue.popleft()
        if board[x][y] in range(1, robot_level):
            heapq.heappush(poses, [count, x, y])
            continue
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not can_go(nx, ny): continue
            if visited[nx][ny]: continue
            visited[nx][ny] = True
            queue.append([[nx, ny], count + 1])

    if not poses: return False
    count, x, y = heapq.heappop(poses)
    robot_pos = [x, y]
    time += count
    return True


def delete_monster():
    global robot_stack, robot_level

    board[robot_pos[0]][robot_pos[1]] = 0
    robot_stack += 1

    if robot_stack == robot_level:
        robot_level += 1
        robot_stack = 0


if __name__ == '__main__':
    while True:
        if not find_food(): break
        delete_monster()

print(time)
