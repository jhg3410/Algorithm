from collections import deque

robot_pos = ([0, 0], [0, 1])
n = -1
board = []


def solution(_board):
    global n, board
    board, n = _board, len(_board)
    visited = [[[] for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append((robot_pos[0], robot_pos[1], 0))
    visited[0][0].append([0, 1])

    while queue:
        pos1, pos2, count = queue.popleft()
        if pos1[0] == n - 1 and pos1[1] == n - 1 or pos2[0] == n - 1 and pos2[1] == n - 1:
            return count
        for rotated in rotate(pos1, pos2):
            small_pos, end_pos = sorted(rotated)
            if end_pos in visited[small_pos[0]][small_pos[1]]:
                continue
            queue.append((small_pos, end_pos, count + 1))
            visited[small_pos[0]][small_pos[1]].append(end_pos)

        for moved in move(pos1, pos2):
            small_pos, end_pos = sorted(moved)
            if end_pos in visited[small_pos[0]][small_pos[1]]:
                continue
            queue.append((small_pos, end_pos, count + 1))
            visited[small_pos[0]][small_pos[1]].append(end_pos)


def is_in(x, y):
    return x in range(n) and y in range(n)


def move(pos1, pos2):
    moved = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        tmp = []
        for pos in [pos1, pos2]:
            nx = pos[0] + dx[i]
            ny = pos[1] + dy[i]
            if not is_in(nx, ny): break
            if board[nx][ny] == 1: break
            tmp.append([nx, ny])
        if len(tmp) == 2:
            moved.append(tmp)
    return moved


def rotate(pos1, pos2):
    rotated = []
    is_horizontal = pos1[0] == pos2[0]

    if is_horizontal:
        for dx, dy in [[1, 0], [-1, 0]]:
            count = 0
            for pos in [pos1, pos2]:
                nx = pos[0] + dx
                ny = pos[1] + dy
                if not is_in(nx, ny): break
                if board[nx][ny] == 1: break
                count += 1
            if count == 2:
                rotated.append([pos1, [pos1[0] + dx, pos1[1]]])
                rotated.append([pos2, [pos2[0] + dx, pos2[1]]])
    else:
        for dx, dy in [[0, 1], [0, -1]]:
            count = 0
            for pos in [pos1, pos2]:
                nx = pos[0] + dx
                ny = pos[1] + dy
                if not is_in(nx, ny): break
                if board[nx][ny] == 1: break
                count += 1
            if count == 2:
                rotated.append([pos1, [pos1[0], pos1[1] + dy]])
                rotated.append([pos2, [pos2[0], pos2[1] + dy]])

    return rotated


if __name__ == '__main__':
    print(solution(_board=[[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
