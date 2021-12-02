def check(s):
    tmp = []
    for i in s:
        if i == '[' or i == '(' or i == '{':
            tmp.append(i)
        elif i == ']':
            if not tmp or tmp[-1] != '[':
                return False
            tmp.pop(-1)
        elif i == ')':
            if not tmp or tmp[-1] != '(':
                return False
            tmp.pop(-1)
        elif i == '}':
            if not tmp or tmp[-1] != '{':
                return False
            tmp.pop(-1)
    if tmp:
        return False
    return True


def solution(s):
    answer = 0
    
    for _ in range(len(s)):
        s = s[1:] + s[:1]
        if check(s):
            answer += 1


    return answer



s = "[](){}"
print(solution(s))