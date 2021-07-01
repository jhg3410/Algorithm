def solution(n, lost, reserve):
    answer = 0
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
            lost.insert(0,"")
    while lost.count("") != 0:
        lost.remove("")
    for i in lost:
        if i -1 in reserve:
            reserve.remove(i-1)
            lost.remove(i)
            lost.insert(0,"")

        elif i +1 in reserve:
            reserve.remove(i+1)
            lost.remove(i)
            lost.insert(0,"")

    while lost.count("") != 0:
        lost.remove("")
    n = n - len(lost)
    answer = n
    return answer