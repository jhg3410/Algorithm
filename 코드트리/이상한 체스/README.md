# 이상한 체스

걸린 시간: 57분

`골4`

[코드트리 | 코딩테스트 준비를 위한 알고리즘 정석](https://www.codetree.ai/training-field/frequent-problems/problems/odd-chess/description?page=3&pageSize=20)

백트래킹 + dx dy 시뮬레이션

좋았던 점

- 체스의 종류와 뱡향에 따른 말의 이동 범위를 빠르게 구현

    ```python
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    def get_routes(piece_type: int, piece_dir: int):
        if piece_type == 0:
            return [piece_dir]
        elif piece_type == 1:
            return [piece_dir, (piece_dir + 2) % 4]
        elif piece_type == 2:
            return [piece_dir, (piece_dir + 1) % 4]
        elif piece_type == 3:
            return [piece_dir, (piece_dir - 1) % 4, (piece_dir + 1) % 4]
        else:
            return [0, 1, 2, 3]
    ```


해설

- 말의 종류와 방향에 따른 실제 이동 방향을 구하는 방식

    ```python
    # 입력으로 주어진 방향에 대해
    # 말의 종류마다 북동남서 방향으로
    # 이동이 가능한지 표시합니다.
    can_move = [
        [],
        [1, 0, 0, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 1, 1]
    ]
    # ...
    
    for i in range(4):
        # 해당 말이 움직일 수 있는 방향인지를 확인합니다.
        # 움직일 수 없다면 pass합니다.
        if not can_move[piece_num][i]:
            continue
        
        # 갈 수 있다면, 끝날때까지 계속 진행합니다.
        # 방향은 face_dir만큼 시계방향으로 
        # 회전했을 때를 기준으로 움직입니다.
        x, y = start_x, start_y
        move_dir = (i + face_dir) % 4;
    ```

  `piece_num == type`

  위처럼 각 말의 종류에 따른 갈 수 있는 방향을 북쪽 기준으로 미리 리스트업 한 뒤,

  추후 실제 방향만큼 이를 돌리면 실제 방향 기준으로 갈 수 있는 방향이 나온다.


- 말들의 방향을 어떻게 백트래킹으로 선정하지를 고민했는데, 말들에게 고유한 번호를 선정하고 할까 하다가,

    ```python
     def find_all_case_type():
        global answer
        global selected
        if len(selected) == my_piece_count:
            answer = min(answer, get_empty_count())
            return
    
        for i in range(4):
            selected.append(i)
            find_all_case_type()
            selected.pop()
    ```

  이처럼 selected 라는 배열에 각각의 방향을 담고, 말들의 이동 범위를 정할 때, selected 를 하나씩 꺼내서 사용


- 해설은 애초에 체스 말의 위치를 저장해서, 말들의 방향은 이차원 배열에 저장하여 접근하도록 풀이

    ```python
    chess_pieces = [
        (i, j)
        for i in range(n)
        for j in range(m)
        if 1 <= board[i][j] and board[i][j] <= 5
    ]
    
    # 말들의 방향을 표시합니다.
    piece_dir = [
        [0 for _ in range(m)]
        for _ in range(n)
    ]
    
    # ...
    for x, y in chess_pieces:
        # 해당 말이 정해진 방향에 있을 때 갈 수 있는 곳들을 전부 표시합니다.
        fill(x, y, board[x][y], piece_dir[x][y])
    ```