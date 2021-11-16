def solution(numbers, k):
    tmp = []

    for num in numbers:
        if len(tmp) == 0:
            tmp.append(num)
        else:
            while tmp and tmp[-1] < num and k != 0:
                tmp.pop()
                k -=1 
            tmp.append(num)
    if k>0:
        tmp = tmp[:len(tmp)-k]
    return ''.join(tmp)
        


print(solution("4177252841",4))