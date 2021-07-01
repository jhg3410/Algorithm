def solution(s):
    answer = ''
    lst = s.split(' ')
    for word in lst:
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += " "
    
    answer = answer[:-1]
    return answer
s = "tRy  hello world   "
print(solution(s))
