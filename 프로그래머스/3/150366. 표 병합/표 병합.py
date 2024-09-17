merge_count = 1
not_merge = -1
EMPTY = ""
board = [[EMPTY for _ in range(50)] for _ in range(50)]
merge_board = [[not_merge for _ in range(50)] for _ in range(50)]
answer = []


def solution(commands):
    for _command in commands:
        command = _command.split()
        type = command[0]
        rest = command[1:]
        if type == "UPDATE" and len(rest) == 3:
            update_value(int(rest[0]) - 1, int(rest[1]) - 1, rest[2])
        elif type == "UPDATE" and len(rest) == 2:
            change_value(rest[0], rest[1])
        elif type == "MERGE":
            merge(int(rest[0]) - 1, int(rest[1]) - 1, int(rest[2]) - 1, int(rest[3]) - 1)
        elif type == "UNMERGE":
            unmerge(int(rest[0]) - 1, int(rest[1]) - 1)
        else:
            print_value(int(rest[0]) - 1, int(rest[1]) - 1)

    return answer


def update_value(x: int, y: int, value: str):
    merge_number = merge_board[x][y]
    if merge_number == not_merge:
        board[x][y] = value
    else:
        for r in range(50):
            for c in range(50):
                if merge_board[r][c] == merge_number:
                    board[r][c] = value


def change_value(value1, value2):
    for r in range(50):
        for c in range(50):
            if board[r][c] == value1:
                board[r][c] = value2


def merge(x1: int, y1: int, x2: int, y2: int):
    global merge_count
    # 같은 셀인 경우 무시
    if merge_board[x1][y1] == merge_board[x2][y2] and merge_board[x1][y1] != not_merge:
        return
    # 새로운 값
    new_value = board[x1][y1] if board[x1][y1] != EMPTY else board[x2][y2]
    merge_number1 = merge_board[x1][y1]
    merge_number2 = merge_board[x2][y2]
    # 2개 모두 병합된 경우가 아니면 두개를 병합
    if merge_number1 == merge_number2 == not_merge:
        merge_board[x1][y1] = merge_count
        merge_board[x2][y2] = merge_count
    # 1이 병합되지 않았고, 2가 병합되었다면 2가 병합된 셀을 찾아서 업데이트
    elif merge_number1 == not_merge:
        merge_board[x1][y1] = merge_count
        for r in range(50):
            for c in range(50):
                if merge_board[r][c] == merge_number2:
                    merge_board[r][c] = merge_count
    # 2이 병합되지 않았고, 1가 병합되었다면 1이 병합된 셀을 찾아서 업데이트
    elif merge_number2 == not_merge:
        merge_board[x2][y2] = merge_count
        for r in range(50):
            for c in range(50):
                if merge_board[r][c] == merge_number1:
                    merge_board[r][c] = merge_count
    # 2개 모두 병합되어 있다면, 2개 모두 병합된 셀을 찾아서 업데이트
    else:
        for r in range(50):
            for c in range(50):
                if merge_board[r][c] == merge_number1 or merge_board[r][c] == merge_number2:
                    merge_board[r][c] = merge_count
    # 모두 병합된 이후, 값을 업데이트
    for r in range(50):
        for c in range(50):
            if merge_board[r][c] == merge_count:
                board[r][c] = new_value
    merge_count += 1


def unmerge(x: int, y: int):
    merge_number = merge_board[x][y]
    pre_value = board[x][y]
    # 병합되지 않았다면 return
    if merge_number == not_merge:
        return
    for r in range(50):
        for c in range(50):
            if merge_board[r][c] == merge_number:
                merge_board[r][c] = not_merge
                board[r][c] = EMPTY

    board[x][y] = pre_value


def print_value(x: int, y: int):
    answer.append("EMPTY" if board[x][y] == EMPTY else board[x][y])


if __name__ == '__main__':
    print(solution(commands=["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean",
                             "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle",
                             "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle",
                             "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group",
                             "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
