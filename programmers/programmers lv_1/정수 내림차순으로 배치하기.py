def solution(n):
    n = list(str(n))
    n.sort(reverse= True)
    return int("".join(n))
    # lst = ''
    # for i in n:
    #     lst += str(i)
    # return int(lst)

print(solution(11234))