# 디버깅

걸린 시간: 52분

`골3`

[코드트리 | 코딩테스트 준비를 위한 알고리즘 정석](https://www.codetree.ai/training-field/frequent-problems/problems/debugging/description?page=3&pageSize=20)

백트래킹 시뮬레이션 문제

좋았던 점

- 설치된 유실선을 1차원 배열로 풀어서 관리

    ```python
    installed = [False for _ in range(h * (n - 1))]
    
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        installed[(a * (n - 1)) + b] = True
    ```

  → 이렇게 한 이유는 백 트래킹할 때, 쉽게 할려고

    ```python
    def find_all_case(limit: int, count: int):
        global fix
        if count == limit:
            if can_fix(): fix = True
            return
    
        for i in range(len(installed)):
            if installed[i]: continue
            installed[i] = True
            find_all_case(limit=limit, count=count + 1)
            installed[i] = False
    ```

  → 이렇게 단순히 1차원 배열에 각 인덱스가 True 가 되는 모든 경우의 수를 탐색


아쉬운 점

- 조합으로 가능한데, 순열로 풀었다…
- 불필요한 연산을 제거할 수 있었다.

    ```python
    def find_all_case(limit: int, count: int, start: int):
        global fix
        if fix:
            return
        if count == limit:
            if can_fix(): fix = True
            return
    
        for i in range(start, len(installed)):
            if installed[i]: continue
            installed[i] = True
            find_all_case(limit=limit, count=count + 1, start=i + 1)
            installed[i] = False
    ```

    - 이처럼 위에 `if fix: return` 문을 넣어서 이미 이전에 답이 구해졌다면 바로 return

- 순열로 풀었을 때 → 조합으로 풀었을 때 → 불필요한 연산 제외했을 때
    - **400ms → 320ms → 178ms**

해설

- 백트래킹의 방식 차이
    - 해설

    ```python
    # 이미 3개를 뽑았거나, 더 이상 뽑을 게 없다면
    # 퇴각합니다.
    if cnt == 3 or curr_idx == len(candidates):
        return
    
    # curr_idx 번째 유실선은 추가하지 않았을 경우
    find_min(curr_idx + 1, cnt)
    
    # curr_idx 번째 유실선을 추가헀을 경우
    # 해당 위치에 유실선을 추가해줍니다.
    a, b = candidates[curr_idx]
    line[a][b] = True
    find_min(curr_idx + 1, cnt + 1)
    line[a][b] = False
    
    ```

  이런 식으로 추가 여부에 따른 각기 재귀를 돌린다.

    - 내 코드

    ```python
    for i in range(start, len(installed)):
        if installed[i]: continue
        installed[i] = True
        find_all_case(limit=limit, count=count + 1, start=i + 1)
        installed[i] = False
    ```

  난 먼저 True 로 다 돈 다음 탈출하면서 False 로 바꾸고, 반복문을 이용해, 계속 재귀를 탐색하는 방식


- 버그가 없는 지 확인하는 방법
    - 내 코드

    ```python
    def can_fix():
        for start_line in range(n):
            current_line = start_line
            for current_row in range(h):
                stand = current_row * (n - 1) + current_line
                pre = current_row * (n - 1) + current_line - 1
                if current_line == 0:
                    if installed[stand]:
                        current_line += 1
                elif current_line == n - 1:
                    if installed[pre]:
                        current_line -= 1
                else:
                    if installed[stand]:
                        current_line += 1
                    if installed[pre]:
                        current_line -= 1
    
            if current_line != start_line:
                return False
    
        return True
    ```

  각 라인을 기준으로 하나씩 내려가면서 이동시켜 주도록 해서 처음 라인과 다르게 내려왔으면 `return False` **(라인이 기준)**

    - 해설

    ```python
    # 직접 어느 위치로 이동하는지를
    # 계산하기 위해 초기값을 설정해줍니다.
    for i in range(1, n + 1):
        num[i] = i
    
    # 유실 선이 있는 경우
    # 해당 위치에 있는 고객의 번호를 서로 교환합니다.
    for a in range(1, h + 1):
        for b in range(1, n):
            if line[a][b]:
                num[b], num[b + 1] = num[b + 1], num[b]
    
    # 전부 자기 자신으로 내려오는지 확인합니다.
    if any([
        num[i] != i
        for i in range(1, n + 1)
    ]):
        return False
    ```

  각 모든 라인에 대해 초기 위치를 정하고, **유실 선을 기준으로** 탐색하면서 선이 존재하면 라인을 변경하는 방식으로 한 번에 확인