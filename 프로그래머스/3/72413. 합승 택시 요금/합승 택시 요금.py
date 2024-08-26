import heapq

cant_go = 10 ** 10


def solution(n, s, a, b, fares):
    answer = cant_go

    min_costs = [[cant_go for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        min_costs[i][i] = 0

    moves = [[] for _ in range(n + 1)]
    for c, d, f in fares:
        moves[c].append([f, d])
        moves[d].append([f, c])

    def dijkstra(start: int):
        pq = []
        distances = [cant_go for _ in range(n + 1)]
        distances[start] = 0
        heapq.heappush(pq, [0, start])

        while pq:
            cumulate_cost, start_node = heapq.heappop(pq)
            for cost, end_node in moves[start_node]:
                new_cost = cumulate_cost + cost
                if distances[end_node] <= new_cost: continue
                heapq.heappush(pq, [new_cost, end_node])
                distances[end_node] = new_cost
                min_costs[start][end_node] = new_cost

    dijkstra(s)
    dijkstra(a)
    dijkstra(b)

    for i in range(1, n + 1):
        answer = min(answer, min_costs[s][i] + min_costs[a][i] + min_costs[b][i])

    return answer


if __name__ == '__main__':
    print(solution(7, 3, 4, 1, fares=[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
    # print(solution(3, 2, 1, 3, fares=[[1, 2, 10], [3, 1, 11]]))
