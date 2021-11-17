from collections import deque
def solution(numbers, target):
    answer = 0
    
    queue = deque()
    queue.append([0,numbers[0]])
    queue.append([0,(-1 * numbers[0])])
    while queue:
        idx,result =  queue.pop()
        idx += 1
        if idx == len(numbers):
            if result == target:
                answer += 1
        else:
            queue.append([idx, result +numbers[idx]])
            queue.append([idx, result -numbers[idx]])
        

    return answer

print(solution([1, 1, 1, 1, 1],3))