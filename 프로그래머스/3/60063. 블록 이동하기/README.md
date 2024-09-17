## **블록 이동하기**

`걸린 시간: 1시간`

LEVEL 3

[블록 이동하기](https://school.programmers.co.kr/learn/courses/30/lessons/60063)

`시뮬레이션 + bfs 문제`

아쉬웠던 점

- 풀다가 코드가 길어지니 맞는지 의심함

좋았던 점

- bfs 로 풀어도 되겠다 하고
- 회전과 이동이 가능한 방법을 모두 고려
- 좌표가 2개니 visited 처리에서 단순히 좌표로 보관하면 최대 30000만개가 저장될 수 있으니 이를 탐색하면 시간초과가 날 것으로 생각
    - → 로봇의 두 좌표 중 무조건 작은 좌표를 구해서, 작은 좌표를 기준으로 `visited[small_pos[0]][small_pos[1]]` 에 큰 좌표들을 넣어서 처리 하면 O(3) 으로 찾을 수 있겠다 생각
    - → 굳

다른 사람 풀이

- 방향을 기반으로 움직이고, visited 를 기록

```python
START = (0, 0, ROW_WISE)

queue = deque([START])
visited = set()
visited.add(START)
```

- 그래서 bfs 를 돌 때 `queue` 도 좌표와 방향으로 계속 움직이고, 회전.
