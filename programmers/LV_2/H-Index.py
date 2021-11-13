from bisect import bisect_right

def solution(citations):
    answer = 0
    citations.sort()

    for i in range(len(citations)+1):
        right = len(citations) - bisect_right(citations,i)
        tmp = right + citations.count(i)
        if  tmp >= i:
            if len(citations)- tmp <= i:
                answer = i

    return answer


print(solution([3, 0, 6, 1, 5]))
