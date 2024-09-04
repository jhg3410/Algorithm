## 양과 늑대

`걸린 시간: 22분`

LEVEL 3

[양과 늑대](https://school.programmers.co.kr/learn/courses/30/lessons/92343)

그래프 탐색 문제 (`dfs`, `bfs`)

Good

- 완탐을 해도 시간안에 해결 가능
- 빠르게 문제 품
- 지금까지 방문한 노드들을 기반으로 갈 수 있는 노드를 탐색(중복은 제외 X)

다른 분의 풀이

- 일반적인 `bfs`

```python
visited.append(child)
is_sheep = infos[child] == 0
search(visited=visited, sheep_count=sheep_count + is_sheep, wolf_count=wolf_count + (not is_sheep))
visited.pop()
```

난 `append` `pop` 으로 재귀간의 이전 상태를 복구했다면 

```python
for move in moves:
    dfs(graph, move, sheep, wolf, moves-set([move]), info)
```

`set` 으로 단순히 빼기 작업으로 항상 새로운 집합을 만들어냄

코드는 간단하지만 항상 새로운 집합을 만들어내서 메모리 측면에선 좋지 않을 듯
