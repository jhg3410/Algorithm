from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False for _ in range(m)] for _ in range(n)]


def can_fire(x: int, y: int):
    return x in range(n) and y in range(m) and not visited[x][y] and board[x][y] != 1


def get_all_case(start: int, count: int):
    global answer

    if count == 3:
        answer = max(answer, bomb())
        return

    for i in range(start, n * m):
        r = i // m
        c = i % m
        if board[r][c] != 0:
            continue
        board[r][c] = 1
        get_all_case(start=i + 1, count=count + 1)
        board[r][c] = 0


def bomb():
    for x in range(n):
        for y in range(m):
            visited[x][y] = False

    for x in range(n):
        for y in range(m):
            if board[x][y] == 2 and not visited[x][y]:
                queue = deque()
                queue.append([x, y])
                visited[x][y] = True
                while queue:
                    fx, fy = queue.popleft()
                    for i in range(4):
                        nx = fx + dx[i]
                        ny = fy + dy[i]
                        if can_fire(nx, ny):
                            queue.append([nx, ny])
                            visited[nx][ny] = True

    count = 0
    for x in range(n):
        for y in range(m):
            if not visited[x][y] and board[x][y] == 0:
                count += 1

    return count


if __name__ == '__main__':
    get_all_case(0, 0)
    print(answer)
