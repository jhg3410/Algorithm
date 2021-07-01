import sys
input = sys.stdin.readline
n = int(input())

lst = []
cnt = 1
op = []
for i in range(n):
    a = int(input())
    while cnt <= a:
        lst.append(cnt)
        op.append("+")
        cnt += 1
    
    if lst[-1] == a:
        lst.pop()
        op.append("-")
    else:
        print("NO")
        quit()
for i in op:
    print(i)
