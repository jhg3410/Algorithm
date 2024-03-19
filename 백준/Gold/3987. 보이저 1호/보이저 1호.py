n, m = map(int, input().split())
board = [input() for _ in range(n)]
x, y = map(lambda x: x - 1, map(int, input().split()))

direction = "URDL"
movePos = [[-1,0], [0,1], [1,0], [0,-1]]

maxTime = 0
answerDirection = 'U'

for i in range(4):
    nx = x
    ny = y
    nDir = direction[i]
    time = 0
    while True:
        time += 1
        nx += movePos[direction.index(nDir)][0]
        ny += movePos[direction.index(nDir)][1]
        if nx not in range(n) or ny not in range(m): break
        if board[nx][ny] == 'C': break
        if nx == x and ny == y and nDir == direction[i]: 
            time = 9999999
            break
        symbol = board[nx][ny]
        if symbol == '.': continue
        if nDir == 'U':
            nDir = 'R' if symbol == '/' else 'L'
        elif nDir == 'R':
            nDir = 'U' if symbol == '/' else 'D'
        elif nDir == 'D':
            nDir = 'L' if symbol == '/' else 'R'
        elif nDir == 'L':
            nDir = 'D' if symbol == '/' else 'U'

    if time > maxTime: 
        maxTime = time
        answerDirection = direction[i]

            
print(answerDirection)
if maxTime == 9999999: print("Voyager") 
else: print(maxTime)