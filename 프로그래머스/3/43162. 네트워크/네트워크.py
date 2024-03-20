def solution(n, computers):
    temp = [i for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if computers[i][j]:
                for k in range(n):
                    if temp[k] == temp[i]:
                        print(i, j, k)
                        temp[k] = temp[j]
    print(temp)
    return len(set(temp))