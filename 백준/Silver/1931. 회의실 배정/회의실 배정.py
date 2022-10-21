n = int(input())
s_list = []

for i in range(n):
    first, second = map(int,input().split())
    s_list.append([first,second])
    
s_list.sort(key = lambda a : a[0])
s_list.sort(key = lambda a : a[1])

count = 0
last = 0

for i,j in s_list:
    if i >= last:
        count += 1
        last = j
print(count)