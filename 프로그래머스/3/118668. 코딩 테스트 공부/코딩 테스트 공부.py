import heapq

LIMIT = 150
answer = 10 ** 10


def solution(_alp, _cop, problems):
    global answer
    need_alp = max(list(map(lambda x: x[0], problems)))
    need_cop = max(list(map(lambda x: x[1], problems)))
    # 기본 증가 추가(1에 1시간)
    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])

    start_alp = _alp
    start_cop = _cop

    need_alp = max(start_alp, need_alp)
    need_cop = max(start_cop, need_cop)
    
    dp = [[10 ** 10 for _ in range(need_cop + 1)] for _ in range(need_alp + 1)]
    dp[start_alp][start_cop] = 0
  

    for alp in range(start_alp, need_alp + 1):
        for cop in range(start_cop, need_cop + 1):
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if alp >= alp_req and cop >= cop_req:
                    new_alp, new_cop = min(need_alp, alp + alp_rwd), min(need_cop, cop + cop_rwd)

                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[alp][cop] + cost)

    return dp[-1][-1]


if __name__ == '__main__':
    print(solution(_alp=0, _cop=0, problems=[[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))
