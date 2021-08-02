n,k = map(int,input().split())

lst = [False] * (n+1)

cnt = 0
for i in range(2,n+1):
    if lst[i] == False:
        lst[i] = True
        cnt += 1
        if cnt == k:
            print(i)
            break
    for j in range(i+i,n+1,i):
        if lst[j] == False:
            lst[j] = True
            cnt += 1
            if cnt == k:
                print(j)
                break
        