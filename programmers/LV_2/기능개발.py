import math

def solution(progresses, speeds):
    answer = []

    days = []

    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) /speeds[i]))

    print(days)
    cnt = 0
    tmp = days[0]
    while days:
        print(tmp)
        if tmp >= days[0]:
            days.pop(0)
            cnt += 1
        else:
            tmp = days[0]
            answer.append(cnt)
            cnt = 0
    answer.append(cnt)

    return answer

print(solution([95, 90, 99, 99, 80, 99],	[1, 1, 1, 1, 1, 1]))