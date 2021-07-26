n = int(input())
lst = [list(map(int,input())) for _ in range(n)]
answer = []

def divide(x,y,n):
    num = lst[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if num != lst[i][j]:
                answer.append("(")
                divide(x,y,n//2)
                divide(x,y+n//2, n//2)
                divide(x+n//2,y, n//2)
                divide(x+n//2,y+n//2, n//2)
                answer.append(")")
                return
    answer.append(str(num))

divide(0,0,n)
print(''.join(answer))



