# 이상한 다트 게임

걸린 시간: 1시간 15분

`골3`

[코드트리 | 코딩테스트 준비를 위한 알고리즘 정석](https://www.codetree.ai/training-field/frequent-problems/problems/odd-dart-game/description?page=2&pageSize=20)

원판 모양이지만 사실 2차원 격자를 가지고 쉽게 풀 수 있는 시뮬레이션 문제

좋았던 점

- 인접 처리를 `bfs` 로 쉽게 푼 점
- 아니면 좌표마다 탐색하여 제거 좌표를 찾은 뒤, 마지막에 다시 업데이트 필요

아쉬운 점

- 문제 이해를 잘못 함
    - 한 번 회전할 때마다 인접 제거, 정규화가 필요한데
    - 모든 회전을 처리한 후 마지막에 인접 제거, 정규화로 오해
    - 그래서 20분 동안 디버깅,,

해설을 읽고

- 회전하는 원판을 찾을 때, 원판 배열은 0부터 시작이지만, 주어지는 k 는 1이 시작 기준이라

    - 아래처럼 처리했는데, 해설에선 매우 쉽게 찾음,,

      ```python
      // 나의 풀이
      for e in range(x, n + 1, x):
          r_x = e - 1
          
      // 해설
      for i in range(n):
          if (i + 1) % x == 0:
      ```

- 2차원 배열의 합을 구하는 코드(여러 줄로 만드니 생각보다 가독성이 나쁘지 않구만)

  ```python
   ans = sum([
      plate[i][j]
      for i in range(n)
      for j in range(m)
      if plate[i][j] != BLANK
  ])
  ```

