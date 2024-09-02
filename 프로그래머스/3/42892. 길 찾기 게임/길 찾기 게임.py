from sys import setrecursionlimit
setrecursionlimit(10**6)

node_info = []
answer = [[], []]


def find_answer(nodes):
    if not nodes: return
    # 루트 찾기(y, idx, number)
    root = (-1, -1, -1)
    for idx, (x, y, number) in enumerate(nodes):
        if y > root[0]:
            root = (y, idx, number)
    root_idx = root[1]
    root_number = root[2]

    answer[0].append(root_number)
    # 루트 왼쪽, 오른쪽 분리
    lefts, rights = nodes[:root_idx], nodes[root_idx + 1:]

    find_answer(lefts)

    find_answer(rights)
    answer[1].append(root_number)


def solution(_nodeinfo):
    global node_info

    node_info = sorted([[x, y, number + 1] for number, (x, y) in enumerate(_nodeinfo)])

    find_answer(nodes=node_info)
    return answer


if __name__ == '__main__':
    print(solution(_nodeinfo=[[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
