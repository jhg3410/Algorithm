import heapq

a, b, n= map(int,input().split())
li= []
end_a, end_b= 0, 0

for _ in range(n):
    t, c, m= input().split()
    t,m = int(t), int(m)
    if c== 'B':
        t = max(end_a,t)
        for i in range(m):
            heapq.heappush(li,[t,'B'])
            t+= a
            end_a= t
    else:
        t = max(end_b,t)
        for i in range(m):
            start= t+(b*i)
            heapq.heappush(li,[start,'R'])
            end_b =start+b

a_do, b_do= [], []

for i in range(1,len(li)+1):
    time, color= heapq.heappop(li)
    if color == 'B':
        a_do.append(i)
    else:
        b_do.append(i)

print(len(a_do)); print(*a_do)
print(len(b_do)); print(*b_do)