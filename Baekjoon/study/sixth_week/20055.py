from collections import deque

n ,k = map(int,input().split())
belt = deque(map(int,input().split()))
robot = deque([0]* n)
ans = 1
while True:
    robot.rotate(1)
    belt.rotate(1)
    robot[n-1] = 0

    for i in range(n-2,-1,-1):
        if robot[i] != 0 and robot[i+1] == 0 and belt[i+1] >= 1:
            belt[i+1] -= 1
            robot[i+1] = robot[i]
            robot[i] = 0
    robot[n-1] = 0

    if robot[0] == 0 and belt[0] != 0:
        robot[0] = 1
        belt[0] -= 1

    cnt = 0
    for i in belt:
        if i == 0:
            cnt += 1
    
    if cnt >= k:
        print(ans)
        break

    ans += 1