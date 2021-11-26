def solution(n):
    answer = [[0 for j in range(i+1)] for i in range(n)]
    
    x= -1 
    y = 0
    k = 1
    for i in range(n):
        for j in range(i,n):
            if i % 3 == 0:
                x += 1
            elif i %3 == 1:
                y+=1
            elif i%3 == 2:
                x -=1
                y -=1
            answer[x][y] = k
            k += 1

    return sum(answer,[])

print(solution(4))