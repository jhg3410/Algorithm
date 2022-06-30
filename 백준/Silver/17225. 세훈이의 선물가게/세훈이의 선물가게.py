a, b, n= map(int,input().split())
a_li= []
b_li= []

for _ in range(n):
    t, c, m= input().split()
    t,m = int(t), int(m)
    if c== 'B':
        if a_li:
            if a_li[-1]+a > t:
                t = a_li[-1]+a
        for i in range(m):
            a_li.append(t+(a*i))
    else:
        if b_li:
            if b_li[-1]+b > t:
                t = b_li[-1]+b
        for i in range(m):
            b_li.append(t+(b*i))

number = 1
a_do= []
b_do= []
for i in range(1,max(max(a_li),max(b_li))+1):
    while True:
        if a_li and a_li[0] == i:
            a_do.append(number)
            a_li.pop(0)
            number+= 1
        else:
            break
    while True:
        if b_li and b_li[0] == i:
            b_do.append(number)
            b_li.pop(0)
            number+=1
        else:
            break

print(len(a_do))
print(*a_do)
print(len(b_do))
print(*b_do)