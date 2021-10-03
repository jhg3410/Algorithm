import sys
input = sys.stdin.readline

N,m,M,T,R = map(int,input().split())

exercise_time = 0
time = 0
x = m # 현재 맥박

if x + T > M:
    print(-1)
else:
    while exercise_time != N:
        if x+T <= M:
            x = x+T
            exercise_time += 1
            time += 1 
        else:
            if x-R >= m:
                x = x-R
            else:
                x = m
            time += 1 
    print(time)