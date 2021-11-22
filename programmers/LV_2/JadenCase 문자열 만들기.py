def solution(s):
    tmp = []
    lst = s.split(' ')
    for word in lst:
        if word != '':
            tmp.append(word[0].upper() + word[1:].lower())
        else:
            tmp.append('')
        
    return ' '.join(tmp)

print(solution("3people   unFollowed me "	))