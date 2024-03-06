n, m = map(int, input().split())
relation = [ [False] * (n + 1) for i in range(n+1)]


for i in range(0, m):
    small, large = map(int, input().split())
    relation[small][large] = True


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if relation[i][k] and relation[k][j]:
                relation[i][j] = True


answer = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if relation[i][j] or relation[j][i]:
            count+=1
    
    if count == n- 1: answer+=1


print(answer)
