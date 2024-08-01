import heapq

r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]


def start_game():
    if len(board) >= len(board[0]):
        increase()
    else:
        rotate_left_45()
        increase()
        rotate_right_45()


def rotate_left_45():
    global board
    max_x = len(board)
    max_y = len(board[0])
    new_board = [[0 for _ in range(max_x)] for _ in range(max_y)]
    for i in range(max_x):
        for j in range(max_y):
            new_board[max_y - 1 - j][i] = board[i][j]

    board.clear()
    for row in new_board:
        board.append(row)


def rotate_right_45():
    global board
    max_x = len(board)
    max_y = len(board[0])
    new_board = [[0 for _ in range(max_x)] for _ in range(max_y)]
    for i in range(max_x):
        for j in range(max_y):
            new_board[j][max_x - 1 - i] = board[i][j]

    board.clear()
    for row in new_board:
        board.append(row)


def increase():
    pq = []
    max_length = 0
    for i in range(len(board)):
        new_row = []
        for num in range(1, 101):
            cnt = board[i].count(num)
            if cnt > 0:
                heapq.heappush(pq, [cnt, num])
        while pq:
            cnt, num = heapq.heappop(pq)
            new_row.append(num)
            new_row.append(cnt)
        # 100 개까지 제한
        board[i] = new_row[:100]
        max_length = max(max_length, len(board[i]))

    # 0 채우기
    for i in range(len(board)):
        rest_count = max_length - len(board[i])
        board[i] += [0 for _ in range(rest_count)]


def is_end():
    if r - 1 not in range(len(board)) or c - 1 not in range(len(board[0])): return False
    return board[r - 1][c - 1] == k


if __name__ == '__main__':
    answer = -1
    if is_end():
        answer = 0
        print(answer)
        exit(0)

    for time in range(1, 101):
        start_game()
        if is_end():
            answer = time
            break
    print(answer)
