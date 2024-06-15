from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
start_x = 0
start_y = 0
n, m = 0, 0
visited = []


def solution(board):
    global start_x, start_y
    global n, m
    global visited
    answer = -1

    n = len(board)
    m = len(board[0])
    visited = [[False] * m for _ in range(n)]
    for x, row in enumerate(board):
        for y, val in enumerate(row):
            if val == 'R':
                start_x = x
                start_y = y
    queue = deque()
    queue.append([start_x, start_y, 0])
    visited[start_x][start_y] = True

    while queue:
        current_x, current_y, count = queue.popleft()
        if board[current_x][current_y] == 'G':
            answer = count
            break

        for i in range(4):
            tmp_x = current_x
            tmp_y = current_y
            while True:
                nx = tmp_x + dx[i]
                ny = tmp_y + dy[i]
                if nx not in range(n) or ny not in range(m) or board[nx][ny] == 'D':
                    if not visited[tmp_x][tmp_y]:
                        queue.append([tmp_x, tmp_y, count + 1])
                        visited[tmp_x][tmp_y] = True
                    break
                tmp_x = nx
                tmp_y = ny

    return answer


if __name__ == '__main__':
    print(solution(board=["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
