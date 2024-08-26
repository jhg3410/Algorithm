## 합승 택시 요금

`걸린 시간: 1시간 30분`

LEVEL 3

[합승 택시 요금](https://school.programmers.co.kr/learn/courses/30/lessons/72413)

좋았던 점

- 해결 방안 빠르게 구상
    - 플로이드 워셜로 각 노드끼리의 최소 비용 계산 → 시작 지점에서 임의의 노드까지 이동 →임의의 노드에서 a, b 목적지 까지 이동 → 이동간의 비용 갱신
    - `s, a, b` 에 대해서만 플로이드 워셜을 돌릴 순 없을까? 생각
        - 하지만 실패,, 따로 따로 플로이드 워셜을 돌리긴 무리

아쉬웠던 점

- 각 지점마다 플로이드 워셜은 불가능하단 걸 미리 알았더라면,,
    - 각 지점마다 다익스트라를 돌리면 됐다..

다른 사람의 풀이

- `s, a, b` 지점을 다익스트라로 돌려, 다른 노드까지의 최소 거리를 계산
    - 플로이드-워셜을 하면 불필요한 노드까지 구하게 된다.
    - 아래처럼!
    
    ```python
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
    ```
