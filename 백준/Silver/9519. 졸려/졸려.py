def solution(s):
    s=list(s)
    for i in range(len(s)//2):
        s.insert((i*2)+1,s.pop())
    return ''.join(s)


n= int(input())
s= input()
pre_s = s
repeat = 0
li= [s]
while True:
    repeat+= 1
    s = solution(s)
    li.append(s)
    if pre_s==s:
        li.pop()
        break
    
cnt= (repeat - (n % repeat)) % repeat
print(li[cnt])
