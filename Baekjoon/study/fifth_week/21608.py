n = int(input())

dic = {}
arr = [[0]*n for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(n*n):
    tmp_lst = list(map(int,input().split()))
    dic[tmp_lst[0]] = tmp_lst[1:]

    x = -1
    y = -1
    max_like = -1
    max_empty = -1
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:  # 비어있다면
                like_st = 0
                empty_st = 0
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] == 0:
                            empty_st += 1
                        if arr[nx][ny] in dic[tmp_lst[0]]:
                            like_st += 1
                if max_like < like_st or (max_like == like_st and max_empty < empty_st):
                    x = i
                    y = j
                    max_like = like_st
                    max_empty = empty_st

    arr[x][y] = tmp_lst[0]


result = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        tmp = arr[i][j]
        for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] in dic[tmp]:
                            cnt += 1
        if cnt == 0:
            result += 0
        else:
            result += 10 ** (cnt-1)

print(result)