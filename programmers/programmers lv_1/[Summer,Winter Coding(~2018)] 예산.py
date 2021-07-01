def solution(d, budget):
    answer = 0
    d.sort()
    sum = 0
    for i in d:
        if i > budget:
            return answer
        answer += 1
        sum += i
        if sum > budget:
            return answer -1
    return answer
