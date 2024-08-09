# 연산자 배치하기

걸린 시간: 25분

`실1`

[코드트리 | 코딩테스트 준비를 위한 알고리즘 정석](https://www.codetree.ai/training-field/frequent-problems/problems/arrange-operator/description?page=3&pageSize=20)

간단한 백트래킹 문제

해설

- 백트래킹
    - 내 코드

    ```python
    def check_all_case():
        if len(selected) == n - 1:
            result = calculate()
            update_answer(result=result)
            return
    
        for i in range(3):
            if operators[i] == 0: continue
            operators[i] -= 1
            selected.append(i)
            check_all_case()
            operators[i] += 1
            selected.pop()
    ```

  이런 식으로 `selected` 배열에 연산자를 담아주었다.

  → 그러면 따로 계산하는 함수에서 `selected` 를 하나씩 빼내어 결과를 계산했다.

    - 해설

  백트래킹 내부에서 계속해서 중간값을 가지는 풀이

    ```python
    # 모든 연산자가 선택됐을 때 만들어진 식의 값을 반환합니다.
    def calculate(num1, num2, operator):
        # 연산자를 순서대로 적용하여 결과 값을 계산합니다.
        if operator == 0:
            return num1 + num2
        elif operator == 1:
            return num1 - num2
        else:
            return num1 * num2
            
            
    def find_min_and_max(cnt, val):
        global min_val, max_val
        
        # 모든 연산자가 선택됐을 때 만들 수 있는 값으로 정답을 갱신해줍니다.
        if cnt == n - 1:
            min_val = min(min_val, val)
            max_val = max(max_val, val)
            return
        
        # 사용 가능한 연산자의 후보들을 탐색합니다.
        for i in range(OPERATOR_NUM):
            if operator_cnt[i]:
                operator_cnt[i] -= 1
                find_min_and_max(cnt + 1, calculate(val, numbers[cnt + 1], i))
                operator_cnt[i] += 1
    ```

  이런식으로 재귀함수 파라미터에 `val`  로 계산값을 받아 다음 재귀로 넘길때마다 계산을 한 뒤에 넘겨준다.

  그래서 모든 연산자가 선택되면 그때의 `val` 은 이미 모든 계산이 완료된 값