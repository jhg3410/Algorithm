# 바이러스 실험

걸린 시간: 45분

`골3`

[코드트리 | 코딩테스트 준비를 위한 알고리즘 정석](https://www.codetree.ai/training-field/frequent-problems/problems/virus-experiment/description?page=3&pageSize=20)

문제에서 하라는대로 하면 되는 시뮬레이션

좋았던 점

- 나이순으로 먼저 진행된다는 점에서 우선순위 큐를 사용하려 했지만, 정렬하는 것과 시간 차이가 크게 없을 것 같아 정렬로 빠르게 변경
    - 오히려 넣을 때 모든 부분에 pq의 Push 를 해야해서 더 오래 걸린다.
    - `pq`: 3806ms, `sort`: 1093ms

해설

- 매우 유사하게 풀었는데 해설은 아래처럼 양분과 바이러스를 다음 사이클에 사용되는 것과 완전 분리

    ```python
    virus = [
        [[] for _ in range(n)]
        for _ in range(n)
    ]
    next_virus = [
        [[] for _ in range(n)]
        for _ in range(n)
    ]
    
    food = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    next_food = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    ```

- 난 `virus`, `food` 각자 하나씩 했는데, 해설처럼 나누면 문제를 푸는 과정에서 사고 정리가 잘 되었을 듯