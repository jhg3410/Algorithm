def solution(n):
    remain = ['4','1','2']

    result = ''
    while n:
        result =  remain[n % 3] + result
        n = n // 3 - (n % 3 == 0)
    
    return result

