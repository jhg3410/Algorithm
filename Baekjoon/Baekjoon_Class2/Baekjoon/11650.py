import sys
input = sys.stdin.readline
n = int(input())

lst = []
for i in range(n):
    lst.append(list(map(int,input().split())))

lst.sort(key= lambda x : x[0])



for x,y in lst:
    print(x,y)

# 5
# 8 23
# 8 -23
# 1 21421
# 1 -2
# 1 11