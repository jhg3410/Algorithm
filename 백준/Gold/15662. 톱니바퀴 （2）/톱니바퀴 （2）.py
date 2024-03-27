from collections import deque

n = int(input())
li = [deque(input()) for _ in range(n)]

for _ in range(int(input())):
    number, direction = map(int,input().split())
    early_direction = direction
    number -= 1
    left = li[number][6]    # 왼쪽의 기준 극
    right = li[number][2]    # 오른쪽의 기준 극
    li[number].rotate(direction)
    # 왼 ( number - 1부터 0까지)
    for i in range(number -1 ,-1,-1):
        if li[i][2] != left:
            left = li[i][6]
            direction *= -1
            li[i].rotate(direction)
        else:
            break
    direction = early_direction
    # 오
    for i in range(number+1,n):
        if li[i][6] != right:
            right = li[i][2]
            direction *= -1
            li[i].rotate(direction)
        else:
            break

answer = 0

for tmp in li:
    if tmp[0] == '1':
        answer += 1

print(answer)