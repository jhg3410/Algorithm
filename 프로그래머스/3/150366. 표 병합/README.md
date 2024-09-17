## 표 병합

`걸린 시간: 54분 21초`

LEVEL 3

[표 병합](https://school.programmers.co.kr/learn/courses/30/lessons/150366)

`시뮬레이션 문제` or `union-find`

(꼼꼼하게 푸는 게 중요, 값이 같다고 모두 병합된 셀이 아니라는 것도 파악하는 게 중요)

시뮬레이션 하듯이 풀었다.

일단 50*50 의 표로 value 를 저장했고

병합을 어떻게 다룰 것인지가 문제였는데, 단순히 3차원 배열로 병합된 좌표들을 집어 넣어도 시간초과가 나진 않을 것 같긴했다.
ex). `[[[2,3], [3,4]], [[1,2], [5,3]]]`

그런데 좀 다르게 병합의 정보를 `번호`로 기억

병합의 정보를 표 형식으로 50*50으로 기억

그래서 각 셀 좌표에 `번호`가 들어간다. 이 번호가 같으면 병합된 셀이라는 의미

![image](https://github.com/user-attachments/assets/b3595f0c-4051-4427-a49b-6b78edbc628a)

이렇게 번호가 들어가 있으면 2끼리 병합된 셀, 1끼리 병합된 셀이라는 의미

이렇게 해서 문제를 풀면 코드가 좀 더 깔끔하고 시간도 더 빠를 것이라 생각

다른 사람의 풀이

- `union - find` 문제라고들 한다.
- `merge` 과정을 부모를 합치면서 병합하는 느낌
    - `merge` 과정이 간단해서 좋은 듯
    - 좌표 기준 업데이트 부모만 변경하는 부분에서 좋을 듯

```python
values = ['' for _ in range(50 * 50)]
parent = [i for i in range(50 * 50)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x1, x2):
    root1 = find(x1)
    root2 = find(x2)

    if not values[root1] and values[root2]:
        parent[root1] = root2
        values[root1] = values[root2]
    else:
        parent[root2] = root1
        values[root2] = values[root1]
        
        
# ...
elif command[0] == 'MERGE':
    r1, c1, r2, c2 = map(lambda x: int(x) - 1, command[1:])

    x1 = r1 * 50 + c1
    x2 = r2 * 50 + c2
    if parent[x1] != parent[x2]:
        union(x1, x2)
```
