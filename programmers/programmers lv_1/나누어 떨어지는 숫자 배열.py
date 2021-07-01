def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0: answer.append(-1)
    else: answer.sort()
    return answer

arr =[3,2,6]
print(solution(arr, 10))