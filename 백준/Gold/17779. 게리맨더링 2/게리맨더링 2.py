def solution(d1, d2, x, y):
    li= [[0]*n  for _ in range(n)]
    # 2
    for i in range(d1+1):    # 2-1
        nx= x+i
        ny= y-i
        li[nx][ny]= 5
    
    for i in range(d2+1):    # 2-2
        nx= x+i
        ny= y+i
        li[nx][ny]= 5

    for i in range(d2+1):    # 2-3
        nx= x+d1+i
        ny= y-d1+i
        li[nx][ny]= 5

    for i in range(d1+1):    # 2-4
        nx= x+d2+i
        ny= y+d2-i
        li[nx][ny]= 5

    # 3
    for i in range(n):
        if li[i].count(5) > 1:
            tmp= -1
            for j in range(n):
                if li[i][j] == 5:
                    if tmp == -1:
                        tmp= j
                    else:
                        for k in range(tmp+1,j):
                            li[i][k] = 5
                        break

    # 4
    for r in range(n):
        for c in range(n):
            if  0 <= r < x+d1 and 0 <= c <= y:      # 4-1
                if not li[r][c]:
                    li[r][c]= 1 
            if  0 <= r <= x+d2 and y < c < n:      # 4-2
                if not li[r][c]:
                    li[r][c]= 2
            if  x+d1 <= r < n and 0 <= c < y-d1+d2:      # 4-3
                if not li[r][c]:
                    li[r][c]= 3 
            if  x+d2 < r < n and y-d1+d2 <= c < n:      # 4-4
                if not li[r][c]:
                    li[r][c]= 4 

    region = [0] * 5
    for r in range(n):
        for c in range(n):
            region[li[r][c]-1] += city[r][c]

    return max(region) - min(region)



n= int(input())
city= [list(map(int,input().split())) for _ in range(n)]
d1, d2, x, y =0, 0, 0, 0
answer = 10**6
# 1
for i in range(n):
    d1= i
    for j in range(n):
        d2= j
        for k in range(n):
            x= k
            for l in range(n):
                y= l
                if  1 <= x+1 < (x+1)+d1+d2 <= n and  1 <= (y+1)-d1 < y+1 < (y+1)+d2 <= n:
                    answer= min(solution(d1,d2,x,y),answer)

print(answer)