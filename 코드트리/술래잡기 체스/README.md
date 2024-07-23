# 술래잡기 체스

걸린 시간: 1시간 44분

`골2`

[코드트리 | 코딩테스트 준비를 위한 알고리즘 정석](https://www.codetree.ai/training-field/frequent-problems/problems/odd-chess2/description?page=2&pageSize=20)

dx, dy + 백트래킹 시뮬레이션 문제 (난 bfs로 해결)

좋았던 점

- 시간 복잡도를 고려했을 때 완탐이 가능하단 걸 빠르게 알아차린 점
- bfs 가 좀 복잡하게 돼서 이게 맞나 의심을 했지만 그래도 적용하고 푼 점

해설을 읽고

- 해설에선

  ```
  board
  ```

  하나로만 모든 기능을 돌아가게했다

    - 내가 이렇게 안 한 이유는, 도둑이 움직일 때 그 도둑의 위치를 n*n 을 모두 탐색하면서 찾고 싶지 않다.

- 그래서 전역 변수가 많았다.

```python
# 도둑의 번호가 4*4 보드 위에 존재
board = [[EMPTY for _ in range(4)] for _ in range(4)]
# 도둑의 위치, 방향을 dict 로 보유
thieves = dict()
tagger_pos = []
tagger_dir = -1
```

- 그러다보니

  ```
  bfs
  ```

  를 돌릴 때마다 deque 에는 아래처럼 항상 새로운 변수를 만들고 넣고 빼고 반복했다.

    - 그래서 메모리 초과를 걱정

```python
for new_board, new_thieves, new_tagger_pos, new_tagger_dir, new_score in possible:
    queue.append([new_board, new_thieves, new_tagger_pos, new_tagger_dir, new_score])
```

- 그런데 해설에선 `board` 하나라 백트래킹을 돌릴 때, board 만 새로 만들어서 저장해두면 됐다.

```python
# 더 탐색을 진행한 이후, 초기 상태로 다시 만들기 위해
# temp 배열에 현재 board 상태를 저장해놓습니다.
temp = [
    [board[i][j] for j in range(n)]
    for i in range(n)
]

# 해당 위치의 도둑말을 잡고
extra_score, next_dir = board[nx][ny];
board[nx][ny], board[x][y] = TAGGER, BLANK

# 모든 도둑말을 움직입니다.
move_all()

# 그 다음 탐색을 진행합니다. 
search_max_score(nx, ny, next_dir, score + extra_score)

# 퇴각시 다시 이전 board의 값을 넣어줍니다.
for i in range(n):
    for j in range(n):
        board[i][j] = temp[i][j]
```

딱히 차이는 없을 듯