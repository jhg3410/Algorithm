import operator

def solution(N, stages):
    answer = []
    temp = {}
    stages.sort()
    cnt = len(stages)
    for i in range(1,N+1):
        if cnt <= 0: 
            temp[i] = 0
            continue
        temp[i] = stages.count(i)  / cnt
        cnt = cnt-stages.count(i)
        
    temp = sorted(temp.items(), key =operator.itemgetter(1), reverse=True)
    
    for key , value in temp:
        answer.append(key)

    return answer


n = 5
stages = [1,2,3]	
print(solution(n,stages))