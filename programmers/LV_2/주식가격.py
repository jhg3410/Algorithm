def solution(prices):
    answer = []

    for i in range(len(prices)):
        for j in range(i,len(prices)):
            if prices[i] > prices[j]:
                break
        answer.append(j-i)
    return answer

print(solution([1, 2, 3, 2, 3]))