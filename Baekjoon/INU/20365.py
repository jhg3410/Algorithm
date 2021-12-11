n = int(input())
lst = list(input())
tmp = False
R_cnt = 1
B_cnt = 1
for i in lst:
    if i == 'B' and tmp == True:
        R_cnt += 1
    if i == 'R':
        tmp = True
    if i == 'B':
        tmp = False
if tmp == True:
    R_cnt += 1

tmp = False

for i in lst:
    if i == 'R' and tmp == True:
        B_cnt += 1
    if i == 'B':
        tmp = True
    if i == 'R':
        tmp = False
if tmp == True:
    B_cnt += 1


print(min(R_cnt,B_cnt))
