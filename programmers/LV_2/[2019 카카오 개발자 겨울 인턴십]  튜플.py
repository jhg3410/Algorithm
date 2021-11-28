def solution(s):
    dic = {}

    tmp = s[2:-2].split("},{")
    for i in tmp:
        lst = (list(map(int,i.split(','))))
        for j in lst:
            if j in dic:
                dic[j] += 1
            else:
                dic[j] = 1

    dic = sorted(dic.items(), key= lambda x : x[1],reverse= True)
    answer = [int(i[0]) for i in dic]
    return answer



s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"		
print(solution(s))