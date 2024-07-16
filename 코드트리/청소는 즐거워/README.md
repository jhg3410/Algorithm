# 청소는 즐거워

걸린 시간: 1시간 22분

`골3`

[코드트리 | 코딩테스트 준비를 위한 알고리즘 정석](https://www.codetree.ai/training-field/frequent-problems/problems/cleaning-is-joyful/description?page=2&pageSize=20)

단순 dx, dy, 나선형 구현 문제

아쉬운 점

- 퍼센트 관리
    - 난 아래처럼 각 퍼센트를 배열에 넣어두고 해당 index 를 기반으로 각 4방향의 내부 배열에 index 에 알맞은 좌표 변화값을 넣어줬다.

    ```python
    percent = [5, 10, 10, 7, 7, 1, 1, 2, 2]
    # 왼, 아래, 오, 위
    percent_dx = [[0, -1, 1, -1, 1, -1, 1, -2, 2],
                  [2, 1, 1, 0, 0, -1, -1, 0, 0],
                  [0, -1, 1, 1, -1, -1, 1, 2, -2],
                  [-2, -1, -1, 0, 0, 1, 1, 0, 0]]
    percent_dy = [[-2, -1, -1, 0, 0, 1, 1, 0, 0],
                  [0, -1, 1, 1, -1, -1, 1, 2, -2],
                  [2, 1, 1, 0, 0, -1, -1, 0, 0],
                  [0, 1, -1, 1, -1, 1, -1, 2, -2]]
    ```

    - 해설에선 아래처럼 관리하고 `dust_ratio[move_dir][i][j]` 이런 식으로 관리하고 있었다.
        - 생성하는데에 걸리는 시간을 고려하면 해설처럼 접근하는 방식이 더 좋은 듯

    ```python
    dust_ratio = [
        [
            [0,  0, 2, 0, 0],
            [0, 10, 7, 1, 0],
            [5,  0, 0, 0, 0],
            [0, 10, 7, 1, 0],
            [0,  0, 2, 0, 0],
        ],
        [
            [0,  0, 0,  0, 0],
            [0,  1, 0,  1, 0],
            [2,  7, 0,  7, 2],
            [0, 10, 0, 10, 0],
            [0,  0, 5,  0, 0],
        ],
        [
            [0, 0, 2,  0, 0],
            [0, 1, 7, 10, 0],
            [0, 0, 0,  0, 5],
            [0, 1, 7, 10, 0],
            [0, 0, 2,  0, 0],
        ],
        [
            [0,  0, 5,  0, 0],
            [0, 10, 0, 10, 0],
            [2,  7, 0,  7, 2],
            [0,  1, 0,  1, 0],
            [0,  0, 0,  0, 0],
        ]
    ]
    ```


- 이동에 대해서
    - 난 아래처럼 1, 1, 2, 2, 3, 3, 4, 4, …n - 1, n - 1, n - 1 이라는 규칙으로 이동을 하고, 방향이 전환되는 방법을 생각해서 아래처럼 구현

    ```python
    for dist in range(1, n):
        for j in range(2):
            for k in range(dist):
                stick_x += dx[stick_direction]
                stick_y += dy[stick_direction]
                sweep()
            stick_direction = (stick_direction + 1) % 4
    
    for _ in range(n - 1):
        stick_x += dx[stick_direction]
        stick_y += dy[stick_direction]
        sweep()
    ```

    - 해설에선 아래처럼 방향이 변경되는 조건과 거리가 증가하는 조건을
        - 방향이 왼쪽 오른쪽이 된 경우로 접근했다.

    ```python
    def end():
        return not curr_x and not curr_y
    
    while not end():
        # move_num 만큼 이동합니다.
        for _ in range(move_num):
            move()
            
            # 이동하는 도중 (0, 0)으로 오게 되면,
            # 움직이는 것을 종료합니다.
            if end():
                break
        
        # 방향을 바꿉니다.
        move_dir = (move_dir + 1) % 4
        # 만약 현재 방향이 왼쪽 혹은 오른쪽이 된 경우에는
        # 특정 방향으로 움직여야 할 횟수를 1 증가시킵니다.
        if move_dir == 0 or move_dir == 2:
            move_num += 1
    
    ```