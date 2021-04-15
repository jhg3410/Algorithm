import heapq
import sys
INF =sys.maxsize

def dijkstra(adjacent,k):

    dist = [INF]*len(adjacent) 

    dist[k] = 0 #  [INF], [0], [INF], [INF] ,[INF], [INF], [INF]

    queue = []
    heapq.heappush(queue,[0,k]) # [[0,k]]

    while queue:
        current_dist , here = heapq.heappop(queue) # [0,k]

        for there,length in adjacent[here].items():  #  k번 노드와 연결된 노드와 거리를 넣는다
            next_dist = dist[here]+ length  # 원래거리 + 새로운 거리

            if next_dist < dist[there]: # dist에 저장값보다 적으면 change
                dist[there] = next_dist
                heapq.heappush(queue,[next_dist,there]) # 그 노드를 추가
    return dist


adjacent = [{},{2:2,3:3,4:6},{6:4},{4:1},{},{},{}]  
dist = dijkstra(adjacent,1)

for d in dist[1:]:
    if d != INF:
        print(d,end=" ")
    else:
        print("INF",end=" ")