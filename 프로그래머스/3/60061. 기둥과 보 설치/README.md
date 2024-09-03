## **기둥과 보 설치**

`걸린 시간: 2시간 50분`

LEVEL 3

[기둥과 보 설치](https://school.programmers.co.kr/learn/courses/30/lessons/60061)

x, y 가 반대이고 좌표가 기반인 시뮬레이션 문제

좋았던 점

- 모든 조건을 빠르게 찾음
- 주어지는 x, y, 좌표를 내 방식으로 변경
- 기둥과 보를 다른 리스트로 가져가서 유무를 판단

```python
# 기둥
board_column = [[False for _ in range(n + 1)] for _ in range(n + 1)]
# 보
board_row = [[False for _ in range(n + 1)] for _ in range(n + 1)]
```

아쉬운 점

- 제한 시간(1시간) 안에 로직은 다 완성하고, 테케도 많이 만들어서 해봤지만…

틀렸던 이유는 좌표에 기둥과 보를 모두 판별해야하는데,

아래처럼 짜버리면, 기둥에서 `continue` 로 넘어가면 보를 확인하지 못하고 넘어가서 문제가 생김

그래서 한 좌표에 기둥과 보가 모두 존재하고, 기둥은 잘 건설되었지만, 보는 그렇지 못한 경우에 틀림

```python
def check_is_ok():
    for x in range(n - 1, -1, -1):
        for y in range(n + 1):
            # 기둥이 있다면
            if board_column[x][y]:
                # 아래가 기둥이면 괜찮다.
                if board_column[x + 1][y]: continue
                # 왼쪽에 보가 있다면 괜찮다.
                if y > 0 and board_row[x][y - 1]: continue
                # 보가 있다면 괜찮다.
                if board_row[x][y]: continue
                return False
            # 보가 있다면
            if board_row[x][y]:
                # 아래가 기둥이면 괜찮다.
                if board_column[x + 1][y]: continue
                # 오른쪽 아래가 기둥이면 괜찮다.
                if board_column[x + 1][y + 1]: continue
                # 양쪽에 보가 있다면 괜찮다.
                if board_row[x][y - 1] and board_row[x][y + 1]: continue
                return False

    return True
```

그래서 다음처럼 변경

```python
def check_is_ok():
    for x in range(n - 1, -1, -1):
        for y in range(n + 1):
            is_column_ok = True
            is_row_ok = True
            # 기둥이 있다면
            if board_column[x][y]:
                is_column_ok = False
                # 아래가 기둥이면 괜찮다.
                if board_column[x + 1][y]: is_column_ok = True
                # 왼쪽에 보가 있다면 괜찮다.
                if y > 0 and board_row[x][y - 1]: is_column_ok = True
                # 보가 있다면 괜찮다.
                if board_row[x][y]: is_column_ok = True
            # 보가 있다면
            if board_row[x][y]:
                is_row_ok = False
                # 아래가 기둥이면 괜찮다.
                if board_column[x + 1][y]: is_row_ok = True
                # 오른쪽 아래가 기둥이면 괜찮다.
                if board_column[x + 1][y + 1]: is_row_ok = True
                # 양쪽에 보가 있다면 괜찮다.
                if board_row[x][y - 1] and board_row[x][y + 1]: is_row_ok = True

            if is_column_ok and is_row_ok:
                continue
            return False

    return True
```
