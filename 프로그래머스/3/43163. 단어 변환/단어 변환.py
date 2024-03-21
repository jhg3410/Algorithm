from collections import deque

def solution(begin, target, words):
    queue = deque()
    queue.append([begin, 0])
    visited = [begin]

    while queue:
        current, count = queue.popleft()
        if current == target: return count
        for word in words:
            if word in visited: continue
            if sum([w!=c for w, c  in zip(word, current)]) == 1:
                queue.append([word, count+1])
                visited.append(word)


    return 0