def solution(s):
    dic = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}

    for key, value in dic.items():
        if value in s:
            s = s.replace(value,str(key))
    
    return int(s)


s = "one4seveneight"
solution(s)