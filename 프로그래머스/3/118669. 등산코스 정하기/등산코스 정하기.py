import heapq

n = -1
undefined = 10 ** 10
top_number = -1
min_intensity = undefined
relations = []
summited = []
gated = []
queue = []


def bfs():
    global min_intensity, top_number
    visited = [undefined for _ in range(n + 1)]

    while queue:
        max_dist, number, start = heapq.heappop(queue)
        if gated[number]:
            if max_dist < min_intensity:
                top_number, min_intensity = start, max_dist
            elif max_dist == min_intensity:
                top_number = min(top_number, start)
            else:
                break
            continue

        for can_go, dist in relations[number]:
            new_dist = max(dist, max_dist)
            if new_dist >= visited[can_go]: continue
            if dist > min_intensity: continue
            heapq.heappush(queue, (new_dist, can_go, start))
            if not gated[can_go]:
                visited[can_go] = new_dist

def solution(_n, paths, gates, summits):
    global n, relations, summited, gated, queue
    n = _n
    relations = [[] for _ in range(n + 1)]
    summited = [False for _ in range(n + 1)]
    gated = [False for _ in range(n + 1)]

    for summit in summits:
        summited[summit] = True

    for gate in gates:
        gated[gate] = True

    for number1, number2, distance in paths:
        if summited[number1]:
            relations[number1].append([number2, distance])
        elif summited[number2]:
            relations[number2].append([number1, distance])
        else:
            relations[number1].append([number2, distance])
            relations[number2].append([number1, distance])

    for summit in summits:
        heapq.heappush(queue, (-1, summit, summit))

    bfs()

    return top_number, min_intensity


if __name__ == '__main__':
    print(solution(_n=6, paths=[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
                   , gates=[1, 3], summits=[5]))
