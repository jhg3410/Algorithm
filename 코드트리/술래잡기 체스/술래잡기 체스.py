from collections import deque

answer_score = 0
score = 0
EMPTY = -10 ** 4
# 도둑의 번호가 4*4 보드 위에 존재
board = [[EMPTY for _ in range(4)] for _ in range(4)]
# 도둑의 위치, 방향을 dict 로 보유
thieves = dict()
tagger_pos = []
tagger_dir = -1
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def is_in(x: int, y: int):
    return x in range(4) and y in range(4)


def remove_thief(thief_number: int):
    x, y = thieves[thief_number][:2]
    thieves.pop(thief_number)
    board[x][y] = EMPTY


def start_game():
    global board, thieves, tagger_pos, tagger_dir, score, answer_score
    init_tagger()
    queue = deque()
    queue.append([board, thieves, tagger_pos, tagger_dir, score])
    while queue:
        board, thieves, tagger_pos, tagger_dir, score = queue.popleft()

        answer_score = max(answer_score, score)
        move_thieves()
        possible = move_tagger()

        for new_board, new_thieves, new_tagger_pos, new_tagger_dir, new_score in possible:
            queue.append([new_board, new_thieves, new_tagger_pos, new_tagger_dir, new_score])

    print(answer_score)


def init_tagger():
    global tagger_pos, tagger_dir, score
    thief_number = board[0][0]
    # 술래 할당
    tagger_pos = [0, 0]
    tagger_dir = thieves[thief_number][2]
    # 도둑 제거
    remove_thief(thief_number)

    score += thief_number


def move_thieves():
    for thief_number in range(1, 17):
        if thief_number not in thieves.keys(): continue
        move_thief(thief_number=thief_number)


def move_thief(thief_number: int):
    x, y, t_dir = thieves[thief_number]
    for i in range(8):
        nx = x + dx[t_dir]
        ny = y + dy[t_dir]
        if not is_in(nx, ny):
            t_dir = (t_dir + 1) % 8
            continue
        if tagger_pos[0] == nx and tagger_pos[1] == ny:
            t_dir = (t_dir + 1) % 8
            continue

        # 기존 칸의 도둑말 업데이트
        changed_number = board[nx][ny]
        if changed_number != EMPTY:
            changed_dir = thieves[changed_number][2]
            thieves[changed_number] = [x, y, changed_dir]
        board[x][y] = changed_number

        # 기준 말 업데이트
        board[nx][ny] = thief_number
        thieves[thief_number] = [nx, ny, t_dir]

        break


def move_tagger():
    results = []
    nx = tagger_pos[0]
    ny = tagger_pos[1]
    while True:
        # 새 객체 생성
        new_board = [[EMPTY for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                new_board[i][j] = board[i][j]
        new_thieves = dict()
        for key, value in thieves.items():
            new_thieves[key] = value.copy()
        new_tagger_dir = tagger_dir
        new_score = score

        nx += dx[new_tagger_dir]
        ny += dy[new_tagger_dir]
        if not is_in(nx, ny): break
        if new_board[nx][ny] == EMPTY: continue
        target_thief = new_board[nx][ny]

        # 보드 최신화
        new_board[nx][ny] = EMPTY
        # 술래 최신화
        new_tagger_pos = [nx, ny]
        new_tagger_dir = new_thieves[target_thief][2]
        # 도둑들 정보 최신화
        new_thieves.pop(target_thief)
        # 점수 최신화
        new_score += target_thief

        results.append([new_board, new_thieves, new_tagger_pos, new_tagger_dir, new_score])

    return results


if __name__ == '__main__':
    for _x in range(4):
        inputs = list(map(int, input().split()))
        for z in range(0, 8, 2):
            # 도둑 번호
            _thief_number, _thief_dir = inputs[z], inputs[z + 1] -1
            _y = z // 2
            board[_x][_y] = _thief_number
            thieves[_thief_number] = [_x, _y, _thief_dir]
    start_game()