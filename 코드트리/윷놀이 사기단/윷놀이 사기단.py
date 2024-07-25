from collections import deque

techs = dict()
ARRIVED = 10 ** 5
# 기본
techs[1] = list(range(2, 41, 2))
change_offset = [4, 9, 14]
# 10에서 이동
techs[2] = [10, 13, 16, 19, 25, 30, 35, 40]
techs[3] = [20, 22, 24, 25, 30, 35, 40]
techs[4] = [30, 28, 27, 26, 25, 30, 35, 40]
# 본인의 테크 트리가 뭔 지(기본은 1)
tech_tree = [1 for _ in range(4)]
# 본인의 테크 트리에서 몇 번째에 있는지
positions = [-1 for _ in range(4)]
score = 0
total_score = 0

moves = list(map(int, input().split()))


def is_duplication(i: int, j: int, tech: int, position: int):
    j_tech = tech_tree[j]
    j_position = positions[j]

    if j_position == -1 or i == j or j_position == ARRIVED: return False
    if position >= len(techs[tech]): return False
    if tech == j_tech and position == j_position: return True
    if techs[tech][position] == 40 and techs[j_tech][j_position] == 40: return True
    if j_tech != 1 and techs[tech][position] == techs[j_tech][j_position]:
        return True


def get_max_score(count: int, logs: list[list[int]]):
    global total_score, score
    # 10번 다 돌았으면 끝
    if count == 10:
        total_score = max(score, total_score)
        return
    # 말 4개를 가지고 탐색
    for i in range(4):
        # 이미 도착했다면 제외
        if positions[i] == ARRIVED:
            continue
        tech = tech_tree[i]
        position = positions[i]
        position += moves[count]

        tmp_tec = tech
        tmp_position = positions[i]
        tmp_score = score

        # 위치가 기준점에 와있다면 테크 변경
        if tech == 1 and position in change_offset:
            if position == 4:
                tech = 2
            elif position == 9:
                tech = 3
            else:
                tech = 4
            position = 0

        # 이동 칸에 이미 다른 말이 있다면 불가능
        impossible = False
        for j in range(4):
            if is_duplication(i, j, tech, position):
                impossible = True
                break
        if impossible:
            continue

        # 테크 변경
        tech_tree[i] = tech
        # 위치 변경
        if position >= len(techs[tech]):
            positions[i] = ARRIVED
        else:
            positions[i] = position
            # 점수 적용
            score += techs[tech][position]

        logs.append([tech, position])

        get_max_score(count + 1, logs)

        tech_tree[i] = tmp_tec
        positions[i] = tmp_position
        score = tmp_score
        logs.pop()


get_max_score(count=0, logs=[])
print(total_score)
