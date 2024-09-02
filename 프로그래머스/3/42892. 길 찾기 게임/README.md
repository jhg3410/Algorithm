## 길 찾기 게임

`걸린 시간: 풀이 참고`

LEVEL 3

[길 찾기 게임](https://school.programmers.co.kr/learn/courses/30/lessons/42892/solution_groups?language=python3)

아쉬운 점

- 예외, 고려 케이스가 너무 많을 줄 알았다.
- 그런데 x,y  값으로만 각 노드들의 왼쪽, 오른쪽 자식들을 판별할 수 있는 문제
- 아래와 같은 모습을 걱정했는데, 이렇게 올 수가 없다. 맨 오른쪽이 `level 2`의 y 값에 오도록 문제가 정의되어 있다.

<img width="246" alt="image" src="https://github.com/user-attachments/assets/1a51b7b6-9868-4735-8059-7088d1f0016e">

---

풀이를 보구  

관건은

- 나보다 왼쪽에 있으면 모두 왼쪽 서브트리(x가 적으면)
- 나보다 오른쪽에 있으면 모두 오른쪽 서브트리

그래서 루트를 찾은다음 x 값으로 나보다 적은 애들은 왼쪽, 큰 애들은 오른쪽으로 해서 계속 서브트리를 기준으로 재귀를 돌리면 된다.

```python
def find_answer(nodes):
    if not nodes: return
    # 루트 찾기(y, idx, number)
    root = (-1, -1, -1)
    for idx, (x, y, number) in enumerate(nodes):
        if y > root[0]:
            root = (y, idx, number)
    root_idx = root[1]
    root_number = root[2]

    answer[0].append(root_number)
    # 루트 왼쪽, 오른쪽 분리
    lefts, rights = nodes[:root_idx], nodes[root_idx + 1:]

    find_answer(lefts)

    find_answer(rights)
    answer[1].append(root_number)
```

요런식으로!

위처럼 하기 위해선 입력으로 받은 nodeinfo 각 x 값으로 오름차순 정렬이 되어있어야 한다.
결국 find_anwer의 파라미터에 들어가는 건 트리(서브)이고, 계속해서 왼쪽 오른쪽을 나누면서 
나눈 영역의 루트가 왼쪽(오른쪽) 자식이 된다.

### 직접 트리 구조를 만들어서

```python
class Node:
    def __init__(self, number, left=None, right=None):
        self.number = number
        self.left = left
        self.right = right
```

이런 식으로 left, right 를 가지는 노드를 만들어서

```python
def make_tree(nodes):
    if not nodes: return
    # 루트 찾기(y, idx, number)
    root = (-1, -1, -1)
    for idx, (x, y, number) in enumerate(nodes):
        if y > root[0]:
            root = (y, idx, number)
    root_idx = root[1]
    root_number = root[2]

    # 루트 왼쪽, 오른쪽 분리
    lefts, rights = nodes[:root_idx], nodes[root_idx + 1:]

    return Node(root_number, left=make_tree(lefts), right=make_tree(rights))
```

이전의 코드에서 바로 재귀를 돌리는 게 아닌 왼쪽 오른쪽이 계속 연결된  `루트 노드`를 반환하도록 구현

```python
def preorder(root_node: Node):
    if root_node is None: return
    answer[0].append(root_node.number)
    preorder(root_node.left)
    preorder(root_node.right)
```

해당 `루트 노드`를 아래처럼 돌리면 끝!
