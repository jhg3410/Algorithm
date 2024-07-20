# 승자독식 모노폴리

걸린  시간: 1시간 31분

`골2`

[코드트리 | 코딩테스트 준비를 위한 알고리즘 정석](https://www.codetree.ai/training-field/frequent-problems/problems/odd-monopoly/description?page=2&pageSize=20)

좋았던 점

- 플레이어의 정보(위치, 방향)와 우선순위, 계약 정보를 어떤 구조로 가져가야할 지를 고민
  - 플레이어를 1차원 리스트에 담아버리면 특정 위치의 플레이어를 알기 위해선 또 플레이어 리스트 탐색이 필요
    - → (n*n) * m * 1000
    - → 400 * 400 * 1000
    - 1억 6천만(시간초과)
  - 그래서 많이 나눴다.

    ```python
    directions = dict()
    priorities = dict()
    # 플레이어의 위치
    position_board = []
    # 계약자의 정보
    contract_board = []
    # 계약수의 정보
    contract_count_board = []
    ```

  이렇게 플레이어마다 키를 부여하고, 그에 따른 방향, 우선순위 정보를 따로 dict 에 저장

  또한 플레이어 위치, 계약자 정보, 계약 기간의 정보는 2차원 배열에 저장


아쉬웠던 점

- 위처럼 많이 나누면 많이 관리하다보니, 문제를 풀다 중간 중간 뇌정지가 오고 실수가 생긴다.
  - 이건 많이 풀어보면 되겠지
- 리스트 쓸 때 조심!!

    ```python
    row = list(map(int, input().split()))
    position_board.append(row)
    contract_board.append(row.copy())
    ```

  처음에 `copy()` 를 안 해서 왜 `contract_board` 의 값이 이상하게 변하지 했었다.


해설을 읽고

- 방향 우선순위를 3차원으로 했다.
  - 번호, 현재 방향, 현재 방향 기준 새로운 방향

  ```python
  # 플레이어 마다 방향 우선순위를 설정합니다.
  for num in range(1, m + 1):
      for curr_dir in range(DIR_NUM):
          dirs = list(map(int, input().split()))
          for i, move_dir in enumerate(dirs):
              next_dir[num][curr_dir][i] = move_dir - 1
  
  ```

- 다음 이동 좌표 찾는 로직

    ```python
    number = position_board[x][y]
    c_dir = directions[number]
    p_dir = priorities[number][c_dir]
    # 계약이 없는 칸에 먼저
    for i in range(4):
        nx = x + dx[p_dir[i]]
        ny = y + dy[p_dir[i]]
        if not is_in(nx, ny): continue
        if contract_board[nx][ny] == 0:
            new_positions[number] = [nx, ny]
            directions[number] = p_dir[i]
            break
    # 계약이 가능한 칸이 없다면 본인이 계약한 땅에
    if number not in new_positions:
        for i in range(4):
            nx = x + dx[p_dir[i]]
            ny = y + dy[p_dir[i]]
            if not is_in(nx, ny): continue
            if contract_board[nx][ny] == number:
                new_positions[number] = [nx, ny]
                directions[number] = p_dir[i]
                break
    ```

  나의 이동하는 새로운 좌표를 찾는 로직은 위와 같다.

  번호, 현재 방향, 그에 따른 우선순위 방향을 가지고

  계약이 가능한 칸 먼저 → 내땅에 이렇게 가는데


- 해설 코드

  ```python
  def can_go(x, y, target_num):
      if not in_range(x, y):
          return False
        
      # target 번호와 contract 번호가 일치한 
      # 경우에만 이동이 가능합니다.
      contract_num, _ = contract[x][y]
      return contract_num == target_num
    
  def next_pos(x, y, curr_dir):
      dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
      num, _ = player[x][y]
    
      # Case 1.
      # 먼저 독점계약을 맺지 않은 공간이 있다면 
      # 우선순위에 따라 그곳으로 이동합니다.
      for move_dir in next_dir[num][curr_dir]:
          nx, ny = x + dxs[move_dir], y + dys[move_dir]
            
          if can_go(nx, ny, EMPTY_NUM):
              return (nx, ny, move_dir)
        
      # Case 2.
      # 인접한 곳이 모두 독점계약을 맺은 곳이라면
      # 우선순위에 따라 그 중 본인이 독점계약한 땅으로 이동합니다.
      for move_dir in next_dir[num][curr_dir]:
          nx, ny = x + dxs[move_dir], y + dys[move_dir]
            
          if can_go(nx, ny, num):
              return (nx, ny, move_dir)
  ```

  로직의 차이는 없지만, 해설은 이렇게 함수로 빼내서 `can_go` 의 인자로 target_num 을 이용해서 깔끔하게 풀었다.