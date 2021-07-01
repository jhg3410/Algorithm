def solution(n):
    answer = 0
    three = ''
    while n != 0:
        three += str(n % 3)
        n //= 3
    k = 0
    for i in three[::-1]:
        answer += int(i) * (3**k)
        k +=1
    return answer

print(solution(45))