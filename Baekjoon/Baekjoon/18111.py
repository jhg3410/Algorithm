def solve(n,cnt):
    while True:
        for i in range(n-1):
            if lst[i] > lst[i+1]:
                lst[i] += 1
                cnt += 1
            elif lst[i] < lst[i+1]:
                lst[i] -= 1
                cnt += 2

    return cnt,lst[0][0]

n,m,b = map(int,input().split())

lst_ = []
lst = []
for i in range(n):  
    lst_.append(list(map(int,input().split())))

for i in lst_:
    for j in i:
        lst.append(j)
cnt = 0

cnt,top = solve(n,cnt)
print(cnt,top)