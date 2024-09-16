## **등산코스 정하기**

`걸린 시간: 2시간 30분(아이디어 참고)`

LEVEL 3

[등산코스 정하기](https://school.programmers.co.kr/learn/courses/30/lessons/118669)

`우선순위 큐 + bfs` or `다익스트라`

`출발 → 봉우리 → 출발`  이렇게 이동한다면 결국 `출발 → 봉우리` 이동과 동일한 루트로 `봉우리 → 출발` 로 온다.

→ 왜냐면 최소니깐 `출발 → 봉우리`에서 최소한의 시간(힘)으로 이동한다면 `봉우리 → 출발` 도 동일해야 한다.

그래서 `출발 → 봉우리` 만 고려해서 가장 짧은 시간(힘)으로 이동하는 구간을 찾으면 된다.

여기서 난 `봉우리 → 출발` 로 반대로 해서 풀었다.

(차이는 크게 없지만 이유는 봉우리 하나씩 bfs 로 찾을 때 작은 순서의 봉우리부터 탐색하면 동일한 intensity 라도 교체할 필요가 없었다.)

여기서 난 봉우리 하나씩 `bfs` 를 돌렸다.

봉우리 하나씩 탐색하면서 갈 수 있는 모든 출발점을 탐색했다.

+ 탐색하면서 이미 이전 `bfs` 에서 탐색했을 때 나온 `min_intensity` 보다 크게 나오면 그냥 해당 탐색을 끝냈다.

→ 이미 `min_intensity` 보다 큰 순간 그 루트는 정답이 될 수 없기에

그런데 **시간초과**가 발생

봉우리가 2.5만개, 출발이 1개, 쉼터가 2.5만개로 있을 때가 최대의 시간이 나오는 케이스라고 생각하고, 풀었는데

그러면 붕우리 하나당 쉼터를 모두 탐색한다고 가정하면

2.5만 * 2.5만 → 6억 2천500만

이라서 프로그래머스에선 시간초과가 안 날 거라고 예측했다.

그런데 시간초과가 발생한 것으로 봐선 `paths` 가 200,000 이기에 

각 bfs 마다 최대 `paths` 의 수만큼 `for` 문을 돌 수도 있기에, 그런 듯 하다.

그래서 찾아본 결과

봉우리를 하나씩 bfs 로 탐색하지 말고, 모든 봉우리를 `queue` 에 넣은 다음 한 번에 돌리는 것

```python
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
            continue

        for can_go, dist in relations[number]:
            new_dist = max(dist, max_dist)
            if new_dist >= visited[can_go]: continue
            if dist > min_intensity: continue
            heapq.heappush(queue, (new_dist, can_go, start))
            if not gated[can_go]:
                visited[can_go] = new_dist

```

이렇게 하면, 변경해야 할 부분은 `visited` 를 단순히 Boolean 으로 고려하면 안되고, 정수값으로 고려해야했다.

이전에 탐색한 부분이라고 해도, 또 탐색할 수 있으니

→ 그렇다고 아래처럼 visited 를 Boolean 으로 두고, for 문 위에 두면 시간 초과가 발생한다.

→ visited 가 늦게 처리되어서, 이미 가지 않아도 되는 부분을 탐색할 수 있어서.

```python
def bfs():
    global min_intensity, top_number
    visited = [False for _ in range(n + 1)]

    while queue:
        max_dist, number, start = heapq.heappop(queue)
        if gated[number]:
            if max_dist < min_intensity:
                top_number, min_intensity = start, max_dist
            elif max_dist == min_intensity:
                top_number = min(top_number, start)
            continue
        visited[number] = True
        for can_go, dist in relations[number]:
            new_dist = max(dist, max_dist)
            if visited[can_go]: continue
            if dist > min_intensity: continue
            heapq.heappush(queue, (new_dist, can_go, start))
```

그리고 우선순위큐를 썼기에 다음과 같이 만약 출발지에 갔는데 해당 `intensity` 가 지금까지 찾은 `min_intensity`  보다 크다면, 그냥 `while` 문을 끝내도 괜찮다. → 그 다음부터 꺼내는 친구들은 무조건 더 클테니

```python
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
```
