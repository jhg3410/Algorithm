n = int(input())
lst = list(map(int,input().split()))
lst_idx = [i for i in range(1,n+1)]
result = []
num = 0
a = lst.pop(0) 
result.append(lst_idx.pop(num))

while len(lst) >0:
    if(a < 0):
        num = (num+a) % len(lst)
    else:
        num = (num+(a-1)) % len(lst)
    a = lst.pop(num)
    result.append(lst_idx.pop(num))
    
for i in result:
    print(i,end=" ")