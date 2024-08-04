# 생명과학부 랩 인턴

걸린 시간: 1시간 17분

`골3`

[코드트리 | 코딩테스트 준비를 위한 알고리즘 정석](https://www.codetree.ai/training-field/frequent-problems/problems/biology-lab-intern/description?page=3&pageSize=20)

dx, dy 시뮬레이션

- 좋았던 점

  먼지들의 이동이 꽤나 번거로운 문제

    - s(속력) 만큼 먼지들이 이동하는데, 최대가 1000
        - → 시간 초과 가능
        - → s 만큼 돌 게 아니라 몫, 나머지로 이동한 위치와 방향 계산

- 해설에서 좋았던 점
    - 먼지 이동 최적화
        - 해설은 아래처럼 s 를 최소한으로 나눈 뒤 해당 값만큼 하나씩 이동했다.

        ```python
        # 위, 아래 방향으로 움직이는 경우
        # 2n - 2번 움직이면 다시 제자리로 돌아오게 되므로
        # 움직여야 할 거리를 2n - 2로 나눴을 때의 나머지 만큼만
        # 움직이게 하면 최적화가 가능합니다.
        if d <= 2:
            s %= (2 * n - 2)
        # 왼쪽, 오른쪽 방향으로 움직이는 경우
        # 2m - 2번 움직이면 다시 제자리로 돌아오게 되므로
        # 움직여야 할 거리를 2m - 2로 나눴을 때의 나머지 만큼만
        # 움직이게 하면 최적화가 가능합니다.
        else:
            s %= (2 * m - 2)
        
        # tuple에 넣을 때
        # 곰팡이 크기 정보를 먼저 넣어, 후에 곰팡이끼리 충돌이 일어날 경우
        # 크기부터 비교하여 최대인 곰팡이를 쉽게 판단할 수 있도록 합니다.
        mold[x - 1][y - 1] = (b, s, d - 1)
        
        ...
        # dist번 한 칸씩 이동하면 됩니다.
            for _ in range(dist):
        ```

        - 아래는 내 코드이다.

        ```python
        # 상하
        if d in [0, 1]:
            tmp = x + (dx[d] * s)
            if abs(tmp // (n - 1)) % 2 == 0:
                # 방향은 그대로
                new_x = tmp % (n - 1)
                new_board[new_x][y].append([s, d, b])
            else:
                new_d = 0 if d == 1 else 1
                new_x = (n - 1) - tmp % (n - 1)
                new_board[new_x][y].append([s, new_d, b])
        # 좌우
        else:
            tmp = y + (dy[d] * s)
            if abs(tmp // (m - 1)) % 2 == 0:
                # 방향은 그대로
                new_y = tmp % (m - 1)
                new_board[x][new_y].append([s, d, b])
            else:
                new_d = 2 if d == 3 else 3
                new_y = (m - 1) - tmp % (m - 1)
                new_board[x][new_y].append([s, new_d, b])
        ```

        - 물론 2n, 2m 만큼 돌지도 않는 내 코드가 더 빠르기야 하겠지만, 코드를 짜는 시간은 해설의 풀이가 훨씬 더 빨랐을 것이라 생각,,

    - 먼지 합체
        - 해설은 먼지를 이동할 때마다 크기값을 비교해, 갱신하면서 합체했다.
        - 하지만 난 다 이동한 뒤, 최댓값을 따로 찾아 반영했다.
            - → 더 간단하고, 불필요한 연산 없이 할 수 있었는데, 설계부터 이동, 합체 로직을 나누다 보니 매몰되어 버린듯하다

    - 초기값
        - 빈 값을 해설은 `BLANK = (-1, -1, -1)` 로 놔둔 뒤, 빈 값을 표시
        - 난 `board = [[None for _ in range(m)] for _ in range(n)]` 처럼 None 으로 표시
            - 그러다보니, 컴파일러가 board 의 내부 타입에 대한 의문점을 계속 제기한다