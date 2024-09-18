import heapq

LIMIT = 150
answer = 10 ** 10


def solution(alp, cop, problems):
    global answer
    need_alp = max(list(map(lambda x: x[0], problems)))
    need_cop = max(list(map(lambda x: x[1], problems)))
    # 기본 증가 추가(1에 1시간)
    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])
    queue = []
    # 소요 시간, 알고력, 코딩력
    heapq.heappush(queue, [0, alp, cop])
    visited = [[10 ** 10 for _ in range(LIMIT + 1)] for _ in range(LIMIT + 1)]
    visited[alp][cop] = 0

    while queue:
        time, c_alp, c_cop = heapq.heappop(queue)
        if c_alp >= need_alp and c_cop >= need_cop:
            return time
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if c_alp >= alp_req and c_cop >= cop_req:
                new_alp, new_cop = min(LIMIT, c_alp + alp_rwd), min(LIMIT, c_cop + cop_rwd)
                new_time = time + cost
                if new_time >= visited[new_alp][new_cop]: continue
                visited[new_alp][new_cop] = time + cost
                heapq.heappush(queue, [time + cost, new_alp, new_cop])


if __name__ == '__main__':
    print(solution(alp=10, cop=10, problems=[[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
