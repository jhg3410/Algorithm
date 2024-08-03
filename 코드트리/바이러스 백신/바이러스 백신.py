from collections import deque

answer = 10 ** 5
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
hospitals = []
virus_count = 0
for _i in range(n):
    for _j in range(n):
        if board[_i][_j] == 2:
            hospitals.append([_i, _j])
        elif board[_i][_j] == 0:
            virus_count += 1
hospitals_len = len(hospitals)


def in_range(x: int, y: int):
    return x in range(n) and y in range(n)


def pick_hospital(picked: list[list[int]], start: int):
    global answer
    if len(picked) == m:
        time = delete_virus(poses=picked)
        answer = min(answer, time)
        return

    for i in range(start, hospitals_len):
        picked.append(hospitals[i])
        pick_hospital(picked=picked, start=i + 1)
        picked.pop()


def delete_virus(poses: list[list[int]]):
    visited = [[False for _ in range(n)] for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    all_time = 0
    cnt = 0
    queue = deque()
    for pos in poses:
        queue.append([pos, 0])
        visited[pos[0]][pos[1]] = True

    while queue:
        (x, y), time = queue.popleft()
        all_time = max(all_time, time)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not in_range(nx, ny): continue
            if visited[nx][ny]: continue
            if board[nx][ny] == 1: continue
            visited[nx][ny] = True
            if board[nx][ny] == 0:
                cnt += 1
                if cnt == virus_count:
                    return time + 1
            queue.append([[nx, ny], time + 1])
    if cnt == virus_count:
        return 0
    return 10 ** 5


if __name__ == '__main__':
    pick_hospital([], 0)
    print(-1 if answer == 10 ** 5 else answer)
