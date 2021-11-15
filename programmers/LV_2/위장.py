def solution(clothes):
    answer = 1

    tmp = {}
    for cloth in clothes:
        if cloth[1] in tmp:
            tmp[cloth[1]] += 1
        else:
            tmp[cloth[1]] = 1

    for i in tmp.values():
        answer *= (i+1)

    return answer - 1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]	))