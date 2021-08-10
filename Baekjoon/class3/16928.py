from collections import deque

n, m = map(int,input().split())
lst = [*range(101)]

for _ in range(n+m):
    x, y = map(int,input().split())
    lst[x] = y
    
cnt_lst = [-10 for _ in range(101)] 

queue = deque()
cnt_lst[1] = 0
queue.append(1)

while queue:
    a = queue.popleft()
    for i in range(1,7):
        b = a + i
        if b > 100:
            continue
        b = lst[b]
        if cnt_lst[b] == -10 or cnt_lst[b] > cnt_lst[a]+1:
            cnt_lst[b] = cnt_lst[a]+1
            queue.append(b)
print(cnt_lst[-1])