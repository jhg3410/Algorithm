n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
selected = []
all_intensity = 0
for _i in range(n):
    for _j in range(n):
        all_intensity += board[_i][_j]

answer = 10 ** 10


def check_all_case(start: int):
    global answer
    if len(selected) == n // 2:
        answer = min(answer, get_diff_intensity())
        return

    for i in range(start, n):
        selected.append(i)
        check_all_case(start=i + 1)
        selected.pop()


def get_diff_intensity():
    morning_intensity = 0
    for i in selected:
        for j in selected:
            morning_intensity += board[i][j]

    evening_jobs = list(filter(lambda x: x not in selected, range(n)))
    evening_intensity = 0
    for i in evening_jobs:
        for j in evening_jobs:
            evening_intensity += board[i][j]

    return abs(evening_intensity - morning_intensity)


if __name__ == '__main__':
    check_all_case(0)
    print(answer)