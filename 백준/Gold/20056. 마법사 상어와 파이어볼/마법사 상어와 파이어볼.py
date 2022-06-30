dx= [-1,-1,0,1,1,1,0,-1]
dy= [0,1,1,1,0,-1,-1,-1]

def divide(fireballs_li):       # 2
    for x, y in fireballs_li:   # 2개 이상인 파이어볼이 위치한 곳
        all_m, all_d,all_s, cnt = 0, 0, 0, 0
        while li[x][y]:
            cnt+= 1
            t_m, t_d, t_s= li[x][y].pop() # 각 속성들
            all_m +=t_m; all_s+= t_s
            if t_d % 2 == 0:
                all_d += 1
        m= all_m // 5                # 나누어진 질량
        if m == 0:  continue
        s= all_s // cnt    # 나누어진 속력
        d= [0,2,4,6] if (all_d==0) or (all_d==cnt) else [1,3,5,7]     # 나누어진 방향
        for i in range(4):  
            li[x][y].append([m,d[i],s])


def move():         # 1
    fireballs_li= []    # 파이어볼이 두개 이상인 곳
    tmp= []     # 이동 할 곳 저장
    for x in range(n):
        for y in range(n):
            while li[x][y]:
                a,b= x,y
                m, d, s = li[a][b].pop()  # 파이어볼
                for _ in range(s):   # 속력만큼  이동
                    a+= dx[d]
                    b+= dy[d]
                    if a< 0 or a>= n:  a= (a+n)%n
                    if b< 0 or b>= n:  b= (b+n)%n
                tmp.append([a,b,m,d,s])
    for x, y, m, d, s in tmp:
        li[x][y].append([m,d,s])        

    for i in range(n):
        for j in range(n):
            if len(li[i][j]) >= 2:
                fireballs_li.append([i,j])

    divide(fireballs_li)



n, M, k= map(int,input().split())
li = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(M):
    r, c, m, s, d= map(int,input().split())
    li[r-1][c-1].append([m,d,s])

for _ in range(k):
    move()

answer= 0
for i in range(n):
    for j in range(n):
        if li[i][j]:
            for m,d,s in li[i][j]:
                answer+= m

print(answer)