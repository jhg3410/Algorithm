from collections import deque

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
max_score = 0


def in_range(x: int, y: int):
    return x in range(n) and y in range(m)


def get_max_score():
    global max_score
    dxs = [0, 1, -1]
    dys = [1, 0, 0]
    _dxs = [0, 1, -1, 0]
    _dys = [1, 0, 0, -1]
    for x in range(n):
        for y in range(m):
            queue = deque()
            queue.append([[x, y], [[x, y]]])

            while queue:
                pos, visited = queue.popleft()
                if len(visited) == 4:
                    max_score = max(max_score, get_score(visited))
                    continue
                for dx, dy in zip(dxs, dys):
                    nx = pos[0] + dx
                    ny = pos[1] + dy
                    if not in_range(nx, ny):
                        continue
                    if [nx, ny] in visited: continue
                    new_visited = visited.copy()
                    new_visited.append([nx, ny])
                    queue.append([[nx, ny], new_visited])
            tmp = [[x, y]]
            for i in range(4):
                nx = x + _dxs[i]
                ny = y + _dys[i]
                if not in_range(nx, ny): continue
                tmp.append([nx, ny])
            if len(tmp) == 4:
                max_score = max(max_score, get_score(tmp))
            elif len(tmp) == 5:
                for j in range(1, 5):
                    tmp_pos = tmp.pop(1)
                    max_score = max(max_score, get_score(tmp))
                    tmp.append(tmp_pos)


def get_score(poses: list[list[int]]):
    score = 0
    for x, y in poses:
        score += board[x][y]
    return score


if __name__ == '__main__':
    get_max_score()
    print(max_score)
