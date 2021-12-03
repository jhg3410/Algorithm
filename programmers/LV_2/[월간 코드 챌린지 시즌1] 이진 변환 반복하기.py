def solution(s):    
    zero_cnt, cnt = 0, 0
    
    while s != '1':
        zero_cnt += s.count('0')
        s = s.replace('0','')
        s = bin(len(s))[2:]
        cnt += 1
    
    return [cnt,zero_cnt]


s = "110010101001"
print(solution(s))