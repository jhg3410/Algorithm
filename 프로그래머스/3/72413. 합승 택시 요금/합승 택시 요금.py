cant_go = 10 ** 10


def solution(n, s, a, b, fares):
    answer = cant_go

    costs = [[cant_go for _ in range(n + 1)] for _ in range(n + 1)]
    for c, d, f in fares:
        costs[c][d] = f
        costs[d][c] = f
    for i in range(1, n + 1):
        costs[i][i] = 0

    # a 에서 모든 좌표까지의 최단 거리
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if costs[i][k] == cant_go or costs[k][j] == cant_go: continue
                costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])

    # for i in range(a, a + 1):
    #     for j in range(1, n + 1):
    #         for k in range(1, n + 1):
    #             if costs[i][j] == cant_go or costs[j][k] == cant_go: continue
    #             costs[i][k] = min(costs[i][k], costs[i][j] + costs[j][k])
    # # b 에서 모든 좌표까지의 최단 거리
    # for i in range(b, b + 1):
    #     for j in range(1, n + 1):
    #         for k in range(1, n + 1):
    #             if costs[i][j] == cant_go or costs[j][k] == cant_go: continue
    #             costs[i][k] = min(costs[i][k], costs[i][j] + costs[j][k])
    # # s 에서 모든 좌표까지의 최단 거리
    # for i in range(s, s + 1):
    #     for j in range(1, n + 1):
    #         for k in range(1, n + 1):
    #             if costs[i][j] == cant_go or costs[j][k] == cant_go: continue
    #             costs[i][k] = min(costs[i][k], costs[i][j] + costs[j][k])
    for i in range(1, n + 1):
        if costs[s][i] == cant_go or costs[a][i] == cant_go or costs[b][i] == cant_go: continue
        answer = min(answer, costs[s][i] + costs[a][i] + costs[b][i])

    # print(costs)
    return answer


if __name__ == '__main__':
    solution(7, 3, 4, 1, fares=[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])
    # print(solution(3, 2, 1, 3, fares=[[1, 2, 10], [3, 1, 11]]))
