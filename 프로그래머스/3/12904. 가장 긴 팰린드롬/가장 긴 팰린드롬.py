def solution(s):
    answer = 0

    for offset in range(len(s), 0, -1):
        for j in range(0, len(s) - offset+1):
            if check_palindrome(s[j: j+offset]):
                return offset

    return answer

def check_palindrome(string):
    for idx in range(len(string)//2):
        behind_idx = len(string)-1-idx
        if not string[behind_idx] == string[idx]: return False
    
    return True
        