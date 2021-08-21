bingo  = [list(map(int,input().split())) for _ in range(5)]
lst = [list(map(int,input().split())) for _ in range(5)]
cnt = 0

def is_bingo(bingo):
    bingo_cnt = 0
    dia_sum  = 0    
    dia_sum2 = 0
    for i in range(5):
        # 가로
        if sum(bingo[i]) == 0:
            bingo_cnt += 1
        col_sum = 0    
        # 세로
        for j in range(5):
            if bingo[j][i] == 0:
                col_sum += 1
        if col_sum == 5:
            bingo_cnt += 1
        # 대각
        if bingo[i][i] == 0:
            dia_sum += 1
        if bingo[i][4-i] == 0:
            dia_sum2 += 1
    if dia_sum == 5:
        bingo_cnt += 1
    if dia_sum2 == 5:
        bingo_cnt += 1
        
    if bingo_cnt >= 3:
        return True
    else:
        return False
        
for i in lst:
    for j in i:
        cnt += 1
        for q in range(5):
            for p in range(5):
                if bingo[q][p] == j:
                    bingo[q][p] = 0
        if is_bingo(bingo) == True:
            print(cnt)
            exit()



