import string
def solution(s, n):
    answer =''
    low = list(string.ascii_lowercase)
    upp = list(string.ascii_uppercase)

    for alp in s:
        print(alp)
        if alp in low:
            a = low.index(alp)+n 
            if a >= len(low):
                answer += low[a - len(low)]
            else:
                answer += low[low.index(alp)+n]
        if alp in upp:
            b = upp.index(alp)+n
            if b >= len(upp):
                answer += upp[b - len(upp)]
            else:
                answer += upp[upp.index(alp)+n]
        else:
            answer += " "

    return answer

s = "a B z"
n = 1
print(solution(s,n))