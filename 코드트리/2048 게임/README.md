걸린 시간: 1시간 3분

골2

[코드트리 | 코딩테스트 준비를 위한 알고리즘 정석](https://www.codetree.ai/training-field/frequent-problems/problems/2048-game/description?page=3&pageSize=20)

백트래킹 + 시뮬레이션

좋았던 점

- 왼쪽, 오른쪽, 위 방향으로 2048 게임 진행을 하지 않고, 아래쪽으로 고정한 뒤 격자를 회전시켜서 나머지 방향을 진행한 점
- 게임 진행 로직을 빠르게 구현

아쉬웠던 점

- 백트래킹 결과마다, 처음 입력받은 격자로 게임을 돌려야 했는데, 실수로 이전의 결과가 반영된 격자로 계속 돌림
    - 디버깅이 좀 걸림

해설

- 백트래킹에서 `append`, `pop` 이 아닌 `index` 로

    ```python
    def get_5_case(dirs: list[int]):
        if len(dirs) == 5:
            start_game(directions=dirs)
            return
    
        for i in range(4):
            dirs.append(i)
            get_5_case(dirs=dirs)
            dirs.pop()
    ```

    - 난 위처럼 append, pop 으로 방향을 추가, 제거

    ```python
    def search_max_num(cnt):
        # 5번 이동할 방향을 정했다면
        # 직접 시뮬레이션을 진행합니다.
        if cnt == NUM_MOVES:
            simulate()
            return
    
        # 4 방향 중 이동할 방향을 선택합니다.
        for i in range(4):
            move_dirs[cnt] = i
            search_max_num(cnt + 1)
    ```

    - 해설은 move_dirs[cnt] 로 갱신하는 방식

- 숫자 떨어뜨리는 방식
    - 나는 `while` 문으로 정말 시뮬레이션으로 맨 밑에 있는 친구부터 가능할 때 까지 내리는 방식
    - 해설은 아래와 같은데,

    ```python
    # 아래로 숫자들을 떨어뜨립니다.
    def drop():
        # next_grid를 0으로 초기화합니다.
        for i in range(n):
            for j in range(n):
                next_grid[i][j] = 0
        
        # 아래 방향으로 떨어뜨립니다.
        for j in range(n):
            # 같은 숫자끼리 단 한번만
            # 합치기 위해 떨어뜨리기 전에
            # 숫자 하나를 keep해줍니다.
            keep_num, next_row = NONE, n - 1
            
            for i in range(n - 1, -1, -1):
                if not grid[i][j]:
                    continue
                
                # 아직 떨어진 숫자가 없다면, 갱신해줍니다.
                if keep_num == NONE:
                    keep_num = grid[i][j];
                
                # 가장 최근에 관찰한 숫자가 현재 숫자와 일치한다면
                # 하나로 합쳐주고, keep 값을 비워줍니다.
                elif keep_num == grid[i][j]:
                    next_grid[next_row][j] = keep_num * 2
                    keep_num = NONE
                    
                    next_row -= 1
                
                # 가장 최근에 관찰한 숫자와 현재 숫자가 다르다면
                # 최근에 관찰한 숫자를 실제 떨어뜨려주고, keep 값을 갱신해줍니다.
                else:
                    next_grid[next_row][j] = keep_num
                    keep_num = grid[i][j]
                    
                    next_row -= 1
            
            # 전부 다 진행했는데도 keep 값이 남아있다면
            # 실제로 한번 떨어뜨려줍니다.
            if keep_num != NONE:
                next_grid[next_row][j] = keep_num
                next_row -= 1
    ```

    - 밑에서 부터 0이 아닌 수를 보고, 그 수가 이제 기준이 되어서 놓을 자리를 선정
    - 해설 코드는 0이 있는 칸(빈칸)을 불필요하게 탐색하지 않기에 더 효율적이라 생각