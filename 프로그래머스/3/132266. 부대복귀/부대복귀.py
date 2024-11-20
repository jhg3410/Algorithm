import heapq

DUMMY = 10 ** 10

def solution(n, roads, sources, destination):
    road_info = [[] for _ in range(n+1)]
    
    for road1, road2 in roads:
        road_info[road1].append(road2)
        road_info[road2].append(road1)
    
    distances = [DUMMY for _ in range(n+1)]
    distances[destination] = 0
    
    pq = []
    # time, current_road
    heapq.heappush(pq, [0, destination])
    
    while pq:
        time, current_road = heapq.heappop(pq)
        for road in road_info[current_road]:
            if distances[road] != DUMMY: continue
            distances[road] = time+1
            heapq.heappush(pq, [time+1, road])
    
    
    answer = list(map(lambda x: -1 if distances[x] == DUMMY else distances[x], sources))
    return answer