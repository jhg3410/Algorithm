# **징검다리 건너기**

걸린 시간: 2일

`LEVEL 3`

[](https://school.programmers.co.kr/learn/courses/30/lessons/64062)

- 좋았던 점
    - k 만큼의 구간동안 가장 큰 값들을 기록하고 모든 구간에서 기록한 값 중 가장 작은 값이 정답이란 걸 유추
    - 시간복잡도를 고려해, 이분탐색을 생각.

- 아쉬운 점
    - 이분탐색을 생각했지만, 틀렸다…

- 풀이 과정

질문 목록을 보고 `O(n)` 을 푸는 방식을 봤다. (슬라이딩 윈도우)

[](https://school.programmers.co.kr/questions/41064)

그런데 좀 다르게 접근했다. 아래처럼 해도 되지 않을까?

앞에서부터 보면서 현재값보다 작으면 지우고, k보다 queue 의 크기가 크면 지우고

이렇게 하면, 결국 queue 의 첫번째 원소가 해당 구간마다 큰 값이라고 판단했다.

```python
def solution(stones, k):
    queue = deque()
    answer = 10 ** 10
    for i in range(len(stones)):
        queue.append(stones[i])

        if len(queue) > k:
            queue.popleft()
        while queue[0] < stones[i]:
            queue.popleft()

        if i < k - 1:
            continue

        print(queue[0])
        answer = min(answer, queue[0])

    return answer
```

그런데 정확성이 반도 안 나오는 걸 보고,, 반례를 찾다가

stones = `200000000, 4, 5, 1, 1, 1`, k = `5`

이렇게 넣었는데

`4` 를 return

정답은 `5`가 return 되어야 한다.

문제는 `while` 문이 였는데, 현재 인덱스의 값을 기준으로 앞에서 부터 지우니 2억과 5 사이에 있는 4가 찍히는 것.

그래서 넣기 전에 큐의 마지막 값이 현재의 값보다 작으면 지우는 방식으로 진행

그런데 이러면 `len(queue) > k` 로 판단할 수가 없다.

stones = `11111 11 22` , k = `2`

로 예시를 들면

1. 11111
2. 11111 11
3. 11111 22

이렇게 되는데 `11111` 은 이미 k 구간을 벗어나기에 없애줘야 한다. 그런데 `len` 으로는 이걸 판단 X

그래서 index 를 기록해서 큐의 맨 앞의 값의 index 가 k 구간을 벗어나면 제거하도록 해야한다.

```python
from collections import deque

def solution(stones, k):
    queue = deque()
    answer = 10 ** 10
    for i in range(len(stones)):
        while queue and queue[-1][0] < stones[i]:
            queue.pop()

        queue.append((stones[i], i))

        if queue[0][1] <= i - k:
            queue.popleft()

        if i < k - 1:
            continue

        answer = min(answer, queue[0][0])

    return answer 
```

굳.
