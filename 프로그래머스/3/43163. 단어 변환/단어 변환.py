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
            diffCount = 0
            for w, c  in zip(word, current):
                if c != w:
                    diffCount +=1
            if diffCount == 1:
                queue.append([word, count+1])
                visited.append(word)


    return 0