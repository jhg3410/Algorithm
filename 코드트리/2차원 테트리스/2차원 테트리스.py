k = int(input())
YELLOW = -1001
RED = -1002
score = 0
yellow_board = [[False for _ in range(4)] for _ in range(6)]
red_board = [[False for _ in range(6)] for _ in range(4)]


def print_info():
    print("---------------------")
    print("input")
    print(t, _x, _y)
    print("---------------------")
    print("yellow")
    for y_r in yellow_board:
        print(y_r)
    print("---------------------")
    print("red")
    for r_r in red_board:
        print(r_r)
    print("---------------------")
    print("score")
    print(score)


def build_block(block_type: int, x: int, y: int):
    global score
    # 보드에 따른 블록의 기준점
    # 노랑은 열(col)이 중요
    # 빨강은 행(row)가 중요
    yellow_poses = [[0, y]]
    red_poses = [[x, 0]]
    if block_type == 1:
        pass
    elif block_type == 2:
        yellow_poses.append([0, y + 1])
        red_poses.append([x, 1])
    else:
        yellow_poses.append([1, y])
        red_poses.append([x + 1, 0])

    while True:
        y_built = False
        r_built = False
        if not y_built:
            y_can_build = True
            for y_pos in yellow_poses:
                y_pos_x = y_pos[0]
                y_pos_y = y_pos[1]
                if not check_can_build(YELLOW, y_pos_x + 1, y_pos_y):
                    y_can_build = False
            if y_can_build:
                yellow_poses = list(map(lambda x: [x[0] + 1, x[1]], yellow_poses))
            else:
                # 세우기
                for y_pos in yellow_poses:
                    yellow_board[y_pos[0]][y_pos[1]] = True
                y_built = True

        if not r_built:
            r_can_build = True
            for r_pos in red_poses:
                r_pos_x = r_pos[0]
                r_pos_y = r_pos[1]
                if not check_can_build(RED, r_pos_x, r_pos_y + 1):
                    r_can_build = False
            if r_can_build:
                red_poses = list(map(lambda x: [x[0], x[1] + 1], red_poses))
            else:
                # 세우기
                for r_pos in red_poses:
                    red_board[r_pos[0]][r_pos[1]] = True
                r_built = True

        if r_built and y_built:
            break

    # 가득찬 블록 제거
    while True:
        delete_row_yellow = check_delete(YELLOW)
        delete_col_red = check_delete(RED)
        if delete_row_yellow != -1:
            delete(YELLOW, delete_row_yellow)

        if delete_col_red != -1:
            delete(RED, delete_col_red)

        if delete_row_yellow == -1 and delete_col_red == -1:
            break

    # 연한 부분의 블록 처리
    for x in range(2):
        for y in range(4):
            if yellow_board[x][y]:
                delete(YELLOW, 5)
                score -= 1
            if red_board[y][x]:
                delete(RED, 5)
                score -= 1


def check_can_build(board_type: int, x: int, y: int):
    if board_type == YELLOW:
        if x not in range(6) or y not in range(4): return False
        return not yellow_board[x][y]
    else:
        if x not in range(4) or y not in range(6): return False
        return not red_board[x][y]


def check_delete(boar_type: int):
    for offset in range(5, 1, -1):
        if boar_type == YELLOW:
            if yellow_board[offset].count(True) == 4:
                # 삭제할 row
                return offset
        else:
            count = 0
            for i in range(4):
                if red_board[i][offset]: count += 1
            # 삭제할 col
            if count == 4:
                return offset
    # 삭제할 곳이 없다면 -1
    return -1


# 보드에 행또는 열을 삭제하고 위의 줄을 채운다. -> 점수 증가
def delete(board_type: int, RC: int):
    global score

    if board_type == YELLOW:
        # 행 제거
        for y in range(4):
            yellow_board[RC][y] = False
        # 위의 칸 한 칸씩 채우기
        for x in range(RC - 1, -1, -1):
            for y in range(4):
                yellow_board[x + 1][y] = yellow_board[x][y]
                yellow_board[x][y] = False
    else:
        # 열 제거
        for x in range(4):
            red_board[x][RC] = False
        # 왼쪽 칸 한 칸씩 채우기
        for y in range(RC - 1, -1, -1):
            for x in range(4):
                red_board[x][y + 1] = red_board[x][y]
                red_board[x][y] = False
    score += 1


if __name__ == '__main__':
    for _ in range(k):
        t, _x, _y = map(int, input().split())
        build_block(block_type=t, x=_x, y=_y)
    block_count = 0
    for _x in range(4):
        for _y in range(4):
            if yellow_board[_x + 2][_y]: block_count += 1
            if red_board[_x][_y + 2]: block_count += 1

    print(score)
    print(block_count)
