def solution(n):
    one_cnt = bin(n).count('1')
    i = n+1
    while True:
        if one_cnt == bin(i).count('1'):
            return i    
        i+= 1
        


print(solution(78))