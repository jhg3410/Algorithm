n = int(input())
lst = [list(map(int,input().split()))for _ in range(n)]
answer = []

def divide(x,y,n):
    paper = lst[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if lst[i][j] != paper:
                for q in range(3):
                    for w in range(3):
                        divide(x+q*(n//3),y+w*(n//3),n//3)
                return
    answer.append(paper)

divide(0,0,n)
print(answer.count(-1))
print(answer.count(0))
print(answer.count(1))