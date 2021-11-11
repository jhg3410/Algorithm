n, m, k = map(int,input().split())
lst = []
for i in range(n):
    lst.append(list(map(int,input().split())))

sum_lst = [0] *n

for i in range(m):
    for j in range(n):
        sum_lst[j] +=lst[j][i]
        if sum_lst[j] >= k:
            print(j+1,i+1)
            exit()