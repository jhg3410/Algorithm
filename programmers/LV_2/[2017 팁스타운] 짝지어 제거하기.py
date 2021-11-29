def solution(s):
    tmp = []

    for char in s:
        if not tmp:
            tmp.append(char)
        else:
            if tmp[-1] == char:
                tmp.pop(-1)
            else:
                tmp.append(char)

    return 1 if not tmp else 0

print(solution('cdcd'))