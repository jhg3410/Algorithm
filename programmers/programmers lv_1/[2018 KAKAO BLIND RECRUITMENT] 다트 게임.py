def solution(dartResult):
    answer = []
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            print(dartResult[i-1])
            if dartResult[i] =='1' and dartResult[i+1] == '0':
                answer.append(10)
                continue
            if dartResult[i] =='0' and dartResult[i-1] == '1':
                continue
            else:
                answer.append(int(dartResult[i]))

        if dartResult[i] == 'S':
            answer[-1]  = int(answer[-1]) ** 1
        if dartResult[i] == 'D':
            answer[-1]  = int(answer[-1]) ** 2
        if dartResult[i] == 'T':
            answer[-1]  = int(answer[-1]) ** 3

        if dartResult[i] == '*' and len(answer) > 1:
            answer[-1] *= 2
            answer[-2] *= 2
        if dartResult[i] == '*'and len(answer) == 1:
            answer[-1] *= 2
        if dartResult[i] == '#':
            answer[-1] *= (-1)
    print(answer)
    return sum(answer)
    

print(solution("0S#10S*10S"))