def solution(a, b):
    answer = ''
    week = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    months = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    sum = 0
    for i in range(a):
        sum += months[i]
    sum = sum + b
    for i in range(7):
        if sum % 7 == i:
            answer += week[i]
    return answer

print(solution(5,24))