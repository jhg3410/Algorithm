def solution(param0):
    tmp = []
    answer = []
    set_tmp =[]
    for i in param0:
        for q in range(1,10):
            if '_v'+str(q) in i:
            
                i= i.replace('_v'+str(q),"")
            
        if '/' in i:
            i = i.replace('/',"")
        i = i[-3:]
        tmp.append(i)
    for x in tmp:
        if x not in set_tmp:
            set_tmp.append(x)
    print(set_tmp)
    for i in set_tmp:
        if tmp.count(i) > 1:
            answer.append(i)
            answer.append(tmp.count(i))
    return answer

print(solution(["/a/c_v2.x","/b/b.x"]))