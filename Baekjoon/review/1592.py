n,m,l = map(int,input().split())
lst = [0] * (n+1)

lst[1] += 1
tmp = 1   
cnt = 1 # 공 횟수 
if m == 1:
    print(cnt)
else:
    while True:
        if lst[tmp] % 2 == 1: # 홀수 일 때
            tmp = (tmp + l) % n
            if tmp == 0:
                tmp = n

        else: # 짝수 일 때
            tmp = (tmp - l) % n 
            if tmp == 0:
                tmp = n 
        lst[tmp] += 1
        if max(lst) == m:
            break
        cnt += 1
    print(cnt)