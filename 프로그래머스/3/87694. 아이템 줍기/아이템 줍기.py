from collections import deque

board = [[0 for _ in range(101)] for _ in range(101)]
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def solution(_rectangle, character_x, character_y, item_x, item_y):
    rectangle = map(lambda x: list(map(lambda y: y * 2, x)), _rectangle)
    for (x1, y1, x2, y2) in rectangle:
        for x in range(x1, x2 + 1):
            board[x][y1] = max(1, board[x][y1])
            board[x][y2] = max(1, board[x][y2])
        for y in range(y1, y2 + 1):
            board[x1][y] = max(1, board[x1][y])
            board[x2][y] = max(1, board[x2][y])
        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                board[x][y] = 2

    answer = bfs(character_x * 2, character_y * 2, item_x * 2, item_y * 2)

    return answer


def bfs(character_x, character_y, item_x, item_y):
    queue = deque()
    queue.append([character_x, character_y, 0])
    board[character_x][character_y] = 2

    while len(queue) != 0:
        (x, y, cnt) = queue.popleft()
        if x == item_x and y == item_y: return cnt // 2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx not in range(1, 101) or ny not in range(1, 101): continue
            if board[nx][ny] != 1: continue
            queue.append([nx, ny, cnt+1])
            board[nx][ny] = 2
            
    return 0