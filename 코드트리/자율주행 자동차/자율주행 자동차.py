n, m = map(int, input().split())
car_x, car_y, car_d = map(int, input().split())
if car_d % 2 != 0:
    car_d = (car_d + 2) % 4
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited = [[False for _ in range(m)] for _ in range(n)]


def can_go(x: int, y: int):
    if visited[x][y]: return False
    if board[x][y] == 1: return False
    return True


def operate():
    global car_x, car_y, car_d
    visited[car_x][car_y] = True

    while True:
        is_moved = False
        for i in range(1, 5):
            nd = (car_d + i) % 4
            nx = car_x + dx[nd]
            ny = car_y + dy[nd]
            if not can_go(nx, ny): continue
            car_x, car_y, car_d = nx, ny, nd
            visited[nx][ny] = True
            is_moved = True
            break
        if not is_moved:
            # 후진
            nd = (car_d + 2) % 4
            nx = car_x + dx[nd]
            ny = car_y + dy[nd]
            if board[nx][ny] == 1: break
            car_x, car_y = nx, ny


def get_answer():
    answer = 0
    for x in range(n):
        for y in range(m):
            if board[x][y] == 1: continue
            if visited[x][y]: answer += 1

    return answer


if __name__ == '__main__':
    operate()
    print(get_answer())
