from itertools import combinations
def solution(numbers):
    answer = []
    lst = list(combinations(numbers,2))
    for i in lst:
        answer.append(sum(i))
    answer = sorted(list(set(answer)))
    
    return answer

numbers = [5,0,2,7]
print(solution(numbers))