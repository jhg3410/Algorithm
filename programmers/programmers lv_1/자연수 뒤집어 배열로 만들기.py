def solution(n):
    answer = []
    n = str(n)
    n = n [::-1]
    for x in n:
        answer.append(int(x))
    return answer