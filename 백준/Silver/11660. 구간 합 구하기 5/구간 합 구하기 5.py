

n, m = map(int, input().split())
board = []
answerPoses = []

for i in range(0, n):
    board.append(list(map(int, input().split())))

for i in range(0, m):
    answerPoses.append(list(map(int, input().split())))

for x in range(0, n):
    for y in range(0, n):
        left = board[x-1][y] if x!= 0 else 0 
        up = board[x][y-1] if y!= 0 else 0
        diagonalSum = board[x-1][y-1] if x != 0 and y != 0 else 0
        board[x][y] += left + up - diagonalSum

def getPrefixSum(x1, y1, x2, y2):
    leftSum = board[x2][y1-1] if y1 !=0 else 0
    upSum = board[x1-1][y2] if x1 != 0 else 0
    diagonalSum = board[x1-1][y1-1] if x1 != 0 and y1 != 0 else 0

    return board[x2][y2] - leftSum - upSum + diagonalSum

for pos in answerPoses:
    print(getPrefixSum(pos[0]-1, pos[1]-1,pos[2]-1,pos[3]-1))


