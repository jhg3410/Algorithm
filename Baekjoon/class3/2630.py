n = int(input())
lst= [(list(map(int,input().split()))) for _ in range(n)]
answer = []

def divide(x,y,n):
    color = lst[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != lst[i][j]:
                divide(x,y,n//2)
                divide(x,y+n//2,n//2)
                divide(x+n//2,y,n//2)
                divide(x+n//2,y+n//2,n//2)
                return
    answer.append(color)

divide(0,0,n)
print(answer.count(0))
print(answer.count(1))