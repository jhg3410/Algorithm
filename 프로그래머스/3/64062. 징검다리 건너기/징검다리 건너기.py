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