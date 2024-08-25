## 자물쇠와 열쇠

`걸린 시간: 1시간 30분`

LEVEL 3

[자물쇠와 열쇠](https://school.programmers.co.kr/learn/courses/30/lessons/60059)

좋았던 점

- 해결 방법을 빠르게 구상
    - key 를 기준으로 한 개를 잡고 4 방향을 돌리면서, 각 자물쇠의 위치를 잡으면
        - 나머지 키들의 위치는 자연스럽게 잡히므로 그때 자물쇠를 풀 수 있는지를 확인
        
        ```python
        for lock_x, lock_y in lock_values:
            for i in range(4):
                for key_x, key_y in rotated_keys[i]:
                    if is_fit(key_pos=[key_x, key_y], lock_pos=[lock_x, lock_y], rotate_count=i):
                        return True
        ```
        
    - key 의 최대 수 == 400, 자물쇠 최대 홈 수 == 400
        - → 400 * 400 * 4(방향)
        - → 640000
        - 64만 케이스에서 내부적으로 또 key 의 갯수만큼 풀 수 있는지 확인
        - → 2억 5천만

아쉬웠던 점

- 디버깅 과정에서 멈칫,,
    - → 처음에 잘 때 잘 짜자,,(푸는 경우를 완벽하게 고려 못 함)
    - → 자물쇠가 모두 1인 경우도 고려해야함

다른 사람의 풀이

- 풀이과정은 유사하나, 내가 추가적인 로직을 검증
    - 좋았던 점의 시간복잡도에서 `2억 5천만번`의 연산을 수행했다고 적었는데,
    - 이거 key 갯수 * 자물쇠 갯수 만큼 돌려서 그랬던 건데, 자물쇠의 홈 모두를 탐색하는 게 아닌 하나만 고려해도 됐다.
        - → 왜냐면
        - A 키가 A 자물쇠 홈을 탐색한 뒤
        - A 키가 B 자물쇠 홈을 탐색한다면?? 이때 다른 키(B,C 등등)가 결국 A 자물쇠 홈에 대응되기 때문에(풀 수 있다면)
        - 그렇기에, 한 자물쇠 홈에 대해 모든 키를 대입하면 된다. → 굳이 모든 자물쇠 홈을 고려할 필요가 X
    
    ```python
    # 기존
    for lock_x, lock_y in lock_values:
        for i in range(4):
            for key_x, key_y in rotated_keys[i]:
                if is_fit(key_pos=[key_x, key_y], lock_pos=[lock_x, lock_y], rotate_count=i):
                    return True
    
    # 변경 후
    for i in range(4):
        for key_x, key_y in rotated_keys[i]:
            if is_fit(key_pos=[key_x, key_y], lock_pos=[lock_values[0][0], lock_values[0][1]], rotate_count=i):
                return True
    
    ```
