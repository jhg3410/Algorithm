n = int(input())
populations = list(map(int, input().split()))
relations = [[] for _ in range(n)]
for i in range(n):
    relations[i] = list(map(lambda x: int(x) - 1, input().split()))[1:]

cases = []
answer = 10 ** 10


def get_case(stand, start, acc: list):
    if len(acc) == stand:
        cases.append(acc.copy())
        return

    for i in range(start, n):
        acc.append(i)
        get_case(stand=stand, start=i + 1, acc=acc)
        acc.pop()


def check(case: list):
    store = [case[0]]
    visited = [case[0]]
    while store:
        num = store.pop()
        for q in relations[num]:
            if q not in visited and q in case:
                store.append(q)
                visited.append(q)

    return sorted(case) == sorted(visited)


if __name__ == '__main__':
    for i in range(n - 1):
        get_case(stand=i + 1, start=0, acc=list())

    for case in cases:
        opposite_case = list(filter(lambda x: x not in case, range(n)))
        if check(case=case) and check(case=opposite_case):
            answer = min(answer, abs(sum(map(lambda x: populations[x], case)) - sum(
                map(lambda x: populations[x], opposite_case))))

    print(answer if answer != 10 ** 10 else -1)
