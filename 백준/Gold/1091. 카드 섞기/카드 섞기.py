def isTrue(li,dic):
    tmp= dict()
    tmp[0] =[]
    tmp[1] =[]
    tmp[2] =[]
    for i in range(n):
        tmp[i%3].append(li[i])
    for idx, value in tmp.items():
        tmp[idx] = sorted(value)
    if dic == tmp:
        return True
    return False


n= int(input())
p= list(map(int,input().split()))
s= list(map(int,input().split()))

dic_p= dict()
dic_p[0] =[]
dic_p[1] =[]
dic_p[2] =[]
for i in range(n):
    dic_p[p[i]].append(i)

card= list(range(n))
pre_card= list(range(n))
cnt= 0
while True:
    if isTrue(card,dic_p):
        break
    cnt+= 1
    tmp= [0] *n
    for i in range(n):
        tmp[s[i]]= card[i]
    card= tmp
    if card== pre_card:
        print(-1)
        exit()
    
print(cnt)