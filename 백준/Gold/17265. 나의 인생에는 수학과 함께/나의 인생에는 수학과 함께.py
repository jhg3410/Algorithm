dx = [0,1]
dy = [1,0]
maxAnswer = -10 ** 5
minAnswer = 10**5
board = []

def changeOpToInt(op):
    if op == '+': return -1
    if op == '-': return -2
    if op == '*': return -3
    return op

def dfs(x, y, sum, op):
    global maxAnswer
    global minAnswer
    if x == n - 1 and y == n - 1:
        maxAnswer = max(maxAnswer, sum)
        minAnswer = min(minAnswer, sum)
        return
    
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx in range(n) and ny in range(n):
            if op == 0:
                dfs(nx, ny, sum, int(board[nx][ny]))
            else:
                val = int(board[nx][ny])
                if op == -1:
                    dfs(nx, ny, sum + val, 0)
                if op == -2:
                    dfs(nx, ny, sum - val, 0)
                if op == -3:
                    dfs(nx, ny, sum * val, 0)
                


n = int(input())
for _ in range(n):
    row = list(map(changeOpToInt, input().split()))
    board.append(row)
dfs(0, 0, int(board[0][0]), op = 0)
    
print(maxAnswer, minAnswer)