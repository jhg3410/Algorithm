import sys
input = sys.stdin.readline

m,n = map(int,input().split())
li = tuple([1]*m for _ in range(m))

def plus(idx,num,cnt):
    if num == 0:
        return idx - cnt
    for _ in range(cnt):
        if idx > 0:
            li[idx][0] += num
            idx -= 1
        else:
            li[0][-idx] += num
            idx -= 1

    return idx

def rest():  
    for x in range(1,m):
        for y in range(1,m):
            li[x][y] = li[0][y]

for _ in range(n):
    num_li = list(map(int,input().split()))
    idx = m-1
    for i in range(3):
        idx = plus(idx,i,num_li[i])
    rest()
    
for i in range(m):
    print(" ".join(map(str, li[i])))