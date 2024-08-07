n, m = map(int, input().split())
hospitals = []
mans = []
for x in range(n):
    row = list(map(int, input().split()))
    for y in range(n):
        if row[y] == 2:
            hospitals.append([x, y])
        if row[y] == 1:
            mans.append([x, y])

selected = []
answer = 10 ** 10


def select_hospital(start: int):
    if len(selected) == m:
        get_distance()
        return

    for i in range(start, len(hospitals)):
        selected.append(hospitals[i])
        select_hospital(i + 1)
        selected.pop()


def get_distance():
    global answer
    total_dist = 0
    for mx, my in mans:
        min_dist = 10 ** 10
        for hx, hy in selected:
            dist = abs(mx - hx) + abs(my - hy)
            if dist < min_dist:
                min_dist = dist
        total_dist += min_dist

    answer = min(answer, total_dist)


if __name__ == '__main__':
    select_hospital(0)
    print(answer)
