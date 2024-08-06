from collections import deque

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
next_board = [[0 for _ in range(n)] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]


def can_mix(x: int, y: int, amount: int):
    return (x in range(n) and y in range(n)
            and not visited[x][y] and abs(board[x][y] - amount) in range(l, r + 1))


def init():
    for x in range(n):
        for y in range(n):
            visited[x][y] = False
            next_board[x][y] = 0


def mix_eggs():
    is_mixed = False
    for x in range(n):
        for y in range(n):
            if visited[x][y]: continue
            visited[x][y] = True
            queue = deque()
            queue.append([x, y])
            mix_poses = [[x, y]]
            total_amount = board[x][y]

            while queue:
                cx, cy = queue.popleft()
                amount = board[cx][cy]
                for dx, dy in zip(dxs, dys):
                    nx = cx + dx
                    ny = cy + dy
                    if not can_mix(nx, ny, amount): continue
                    visited[nx][ny] = True
                    mix_poses.append([nx, ny])
                    total_amount += board[nx][ny]
                    queue.append([nx, ny])

            amount = total_amount // len(mix_poses)
            if len(mix_poses) > 1: is_mixed = True
            for mx, my in mix_poses:
                next_board[mx][my] += amount

    if not is_mixed: return False

    for x in range(n):
        for y in range(n):
            board[x][y] = next_board[x][y]

    return True


if __name__ == '__main__':
    time = 0
    while mix_eggs():
        init()
        time += 1

    print(time)
