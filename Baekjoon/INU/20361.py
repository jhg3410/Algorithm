n,x,k = map(int,input().split())
lst = [0]*n
lst[x-1] = 1

for i in range(k):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    lst[a] , lst[b] = lst[b], lst[a]

print(lst.index(1)+1)