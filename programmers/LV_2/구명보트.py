from collections import deque

def solution(peoples, limit):
    answer = 0
    peoples.sort()
    q = deque(peoples)

    while q:
        print(q,answer)
        if len(q) == 1:
            q.pop()
            answer += 1
        else:
            if q[0] + q[-1] <= limit:
                q.pop(), q.popleft()
            else:
                q.pop()
            answer+=1

    return  answer

print(solution([80, 50, 20, 50]	,100))