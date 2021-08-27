from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque()
    # for indx , value in enumerate(priorities):
    #     queue.append((value,indx))
    # print(queue)
    d = deque([(v,i) for i,v in enumerate(priorities)])
    # print(d)
    while len(d): 
        tmp = d.popleft()
        if  d and tmp[0] < max(d)[0]:    
            d.append(tmp)
        else:
            answer += 1
            if tmp[1] == location:
                break
    return answer

solution([2, 1, 3, 2],2)