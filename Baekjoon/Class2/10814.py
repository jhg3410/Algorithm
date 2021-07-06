n = int(input())

lst = []

for i in range(n):
    lst.append(input().split())

lst.sort(key= lambda x: int(x[0]))
for i in lst:
    print(i[0],i[1])

