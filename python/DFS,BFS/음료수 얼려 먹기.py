
def solve(x,y):
    if x <= -1 or x >= N  or y <= -1 or y >= M:
        return False
    
    if graph[x][y] == 0:

        graph[x][y] = 1
        solve(x+1,y)
        solve(x,y+1)
        solve(x-1,y)
        solve(x,y-1)
        return True

    return False


N, M = map(int,input().split())  # 4, 5

graph = []
for _ in range(N):
    graph.append(list(map(int,input())))

result = 0

for i in range(N):
    for j in range(M):
        if solve(i,j) == True:
            result += 1

print(result)


