n = int(input())
lst = list(map(int,input().split()))
result = [0] *n

for i in range(len(lst)):
    cnt = 0 
    for j in range(len(result)):
        if cnt == lst[i] and result[j] == 0:
            result[j] = i+1
            print(result)
            break
        elif result[j] == 0:
            cnt += 1
        
print(*result)
