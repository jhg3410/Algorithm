# 방화벽 설치하기

걸린 시간: 26분

`골4`

[코드트리 | 코딩테스트 준비를 위한 알고리즘 정석](https://www.codetree.ai/training-field/frequent-problems/problems/firewall-installation/description?page=3&pageSize=20)

백트래킹 + bfs 문제

해설

- 백트래킹 과정의 차이
    - 해설 - 방화벽 놓을 위치를 정할 때, 넣을 수 있는 위치를 따로 배열에 넣어두고,
      백트래킹에선 해당 배열에서 3개씩 빼는 로직
    - 나 - `n*m` 을 가지고 row, column 을 구해서 바로 2차원 배열에 방화벽을 달아주는 방식

    ```python
    def get_all_case(start: int, count: int):
        global answer
    
        if count == 3:
            answer = max(answer, bomb())
            return
    
        for i in range(start, n * m):
            r = i // m
            c = i % m
            if board[r][c] != 0:
                continue
            board[r][c] = 1
            get_all_case(start=i + 1, count=count + 1)
            board[r][c] = 0
    
    ```