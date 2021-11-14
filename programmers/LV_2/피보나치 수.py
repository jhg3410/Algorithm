def solution(n):
    answer = [0,1]

    for i in range(2,n+1):
        answer.append(answer[-1]+answer[-2])

    return (answer[-1] % 1234567)

print(solution(4))