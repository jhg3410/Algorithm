# 타협점을 맞춰서 줄이고 늘리고를 맞게끔해야하는데 그걸 생각안하고 예제만 보고
# 최솟값에 맞춰 내리면 내리기면하고 최대값에 맞춰 늘리면 늘리기만해서 틀림
import copy
import sys
input = sys.stdin.readline

def increase(n,m,max_,cnt):
    for i in range(n):
        for j in range(m):
            if lst_1[i][j] < max_:
                while lst_1[i][j] != max_:
                    lst_1[i][j] += 1
                    cnt += 1

    return cnt,max_

def decrease(n,m,min_,cnt):
    for i in range(n):
        for j in range(m): 
            if lst_2[i][j] > min_:
                while lst_2[i][j] != min_:
                    lst_2[i][j] -= 1
                    cnt += 2 
    return cnt,min_

n,m,b = map(int,input().split())
lst_1 = []
for i in range(n):
    lst_1.append(list(map(int,input().split())))

lst_2 = copy.deepcopy(lst_1)

ma_lst = max(lst_1)
max_ =max(ma_lst)

mi_lst = min(lst_1)
min_ =min(mi_lst)

cnt = 0

cnt_1,result_1 = increase(n, m, max_,cnt)

cnt_2,result_2 = decrease(n, m, min_,cnt)

if cnt_1 > b:
    print(cnt_2,result_2)
else:
    if cnt_1<cnt_2: print(cnt_1,result_1)
    else: print(cnt_2,result_2)
    