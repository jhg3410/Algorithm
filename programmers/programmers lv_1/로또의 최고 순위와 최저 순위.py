def solution(lottos, win_nums):
    answer = []

    for q in range(2):
        cnt = 0
        if q == 1:
            cnt += lottos.count(0)
        for i in win_nums:
            if i in lottos:
                cnt += 1

        if cnt == 6:
            answer.append(1)
        elif cnt == 5:
            answer.append(2)
        elif cnt == 4:
            answer.append(3)
        elif cnt == 3:
            answer.append(4)
        elif cnt == 2:
            answer.append(5)
        else:
            answer.append(6)
        
    answer.sort()
    return answer


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos,win_nums))