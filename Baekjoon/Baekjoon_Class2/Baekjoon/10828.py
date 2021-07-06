import sys
input = sys.stdin.readline

n = int(input())

lst = []

result_lst = []

for i in range(n):
    lst.append(input().split())

for i in lst:
    if len(i) >1:
        i[1] = int(i[1])
        result_lst.append(i[1])
    if i[0] == "pop":    
        if len(result_lst) == 0:
            print(-1)
        else: 
            print(result_lst.pop())
    if i[0] == "size":
        print(len(result_lst))
    
    if i[0] == "empty":
        if len(result_lst) == 0:
            print(1)
        else:
            print(0)

    if i[0] == "top":
        if len(result_lst) == 0:
            print(-1)
        else:
            print(result_lst[len(result_lst)-1])
