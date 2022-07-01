end= 21
yut_li= {1:1, 2:2, 3:3, 4: 4, 0:5}
score= 0
cnt= 10
isShortCut= False
isWin= False
while cnt != 0:
    yut= input()
    cnt-= 1
    back_side= yut.count('0')
    if back_side == 4 or  back_side == 0:
        cnt+= 1
    score += yut_li[back_side]
    
    if score >= end:
        print("WIN")
        isWin= True
        break

    if score== 5:
        if not isShortCut:
            isShortCut= True
    if score== 8:
        if isShortCut== True:
            end= 4
            score= 0
            
    if score== 11:
        if isShortCut== True:
            end= 6
            score= 0
            
    if score== 10:
        if not isShortCut:
            end= 7
            score= 0
            isShortCut= True
    
    
if not isWin:
    print("LOSE")