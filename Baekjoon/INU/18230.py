n,a,b = map(int,input().split())
one_lst = sorted(list(map(int,input().split())),reverse= True)
two_lst = sorted(list(map(int,input().split())),reverse= True)
cnt = 0

if n %2 == 1:
    cnt += one_lst.pop(0)
    n -=1 

for _ in range(n//2):
    tmp1,tmp2 = 0,0
    if len(one_lst)>1:
        tmp1 = (one_lst[0] + one_lst[1])
    if len(two_lst)>0:
        tmp2 = two_lst[0]
    cnt+= (one_lst.pop(0)+one_lst.pop(0)) if tmp1> tmp2 else two_lst.pop(0)

print(cnt)