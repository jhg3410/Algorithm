import heapq

n, m, k = map(int, input().split())
# 죽은 바이러스들
died_viruses = [[[] for _ in range(n)] for _ in range(n)]
# 바이러스들
viruses = [[[] for _ in range(n)] for _ in range(n)]
# 증가하는 양분 크기
increase_food = [list(map(int, input().split())) for _ in range(n)]
# 현재 양분
foods = [[5 for _ in range(n)] for _ in range(n)]
# 바이러스 추가
for _ in range(m):
    r, c, _age = map(int, input().split())
    viruses[r - 1][c - 1].append(_age)


def init():
    for x in range(n):
        for y in range(n):
            died_viruses[x][y].clear()


def eat_food():
    for x in range(n):
        for y in range(n):
            if not viruses[x][y]: continue
            new_virus = []
            for idx, age in enumerate(sorted(viruses[x][y])):
                # 섭취
                if age <= foods[x][y]:
                    foods[x][y] -= age
                    new_virus.append(age + 1)
                else:
                    died_viruses[x][y].append(age)
            viruses[x][y] = new_virus


def change_virus_to_food():
    for x in range(n):
        for y in range(n):
            if not died_viruses[x][y]: continue
            for age in died_viruses[x][y]:
                foods[x][y] += age // 2


def breed():
    dxs = [-1, -1, -1, 1, 1, 1, 0, 0]
    dys = [1, 0, -1, 1, 0, -1, 1, -1]
    for x in range(n):
        for y in range(n):
            if not viruses[x][y]: continue
            for age in viruses[x][y]:
                if age % 5 == 0:
                    for dx, dy in zip(dxs, dys):
                        nx = x + dx
                        ny = y + dy
                        if nx not in range(n) or ny not in range(n): continue
                        viruses[nx][ny].append(1)


def grow():
    for x in range(n):
        for y in range(n):
            foods[x][y] += increase_food[x][y]


def get_answer():
    answer = 0
    for x in range(n):
        for y in range(n):
            answer += len(viruses[x][y])

    return answer


if __name__ == '__main__':
    for _ in range(k):
        init()
        eat_food()
        change_virus_to_food()
        breed()
        grow()
    print(get_answer())
