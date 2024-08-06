# 전투 로봇

걸린 시간: 50분

`골3`

[코드트리 | 코딩테스트 준비를 위한 알고리즘 정석](https://www.codetree.ai/training-field/frequent-problems/problems/fighting-robot/description?page=3&pageSize=20)

간단한 bfs 문제

아쉬웠던 점

> 가장 가까운 거리의 없앨 수 있는 몬스터가 하나 이상이라면 가장 위에 존재하는 몬스터를, 가장 위에 존재하는 몬스터가 여럿이라면 가장 왼쪽에 존재하는 몬스터부터 없앱니다.
>
- 위의 조건에 대해 dx, dy 를 `상, 좌, 우, 하` 순서로 bfs 탐색해서 처음 발견하는 게 우선순위가 가장 높은 몬스터라고 판단했다.
    - 그런데 예외로 [← ←] 얘보다  [→ ↑] 가 더 우선순위가 높다.
    - 그런데 위와 같이 하면 [← ←] 가 먼저 나오게 된다.
    - 그래서 우선순위큐로 변경해서 해결

해설

- 로봇의 이동 거리를 bfs 에서 step 이란 이중 배열에 담았다.
    - 이러면 로봇에서부터 각 좌표까지의 최단 거리를 구한다.

    ```kotlin
    step = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    ```

- 난 `queue` 내부에 담았다.

    ```kotlin
    queue.append([robot_pos, 0])
    ```