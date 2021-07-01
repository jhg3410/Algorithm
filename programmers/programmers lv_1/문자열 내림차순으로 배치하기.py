def solution(s):

    s = sorted(s,reverse=True)
    return ''.join(s)

print(solution("Zbcdefg"))