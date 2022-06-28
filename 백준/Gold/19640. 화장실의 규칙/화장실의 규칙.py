import heapq

def solution(m,deka,line):
    wc = []
    cnt = 0
    for i in range(m):
        if line[i]:
            heapq.heappush(wc,line[i][0])
        
    while True:
        d,h,row,column = heapq.heappop(wc)
        if [row, column] == deka:
            return cnt
        line[row].pop(0)
        if line[row]:
            heapq.heappush(wc,line[row][0])
        cnt += 1

n, m, k = map(int,input().split())
deka= [k%m, k//m]
line= [[] for _ in range(m)]

for i in range(n):
    d, h = map(int,input().split())
    row = i % m
    line[row].append([-d, -h,row,i//m])

print(solution(m,deka,line))