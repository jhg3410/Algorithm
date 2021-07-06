def solution(board, moves):
    answer = 0
    temp = []
    for moving in moves:
        for lst in board:
            if lst[moving-1] != 0:
                temp.append(lst[moving -1])
                lst[moving-1] = 0
                if len(temp) > 1:
                    if temp[-1] == temp[-2]:
                        temp.pop()
                        temp.pop()
                        answer += 2
                break
            
                

    return answer



board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board,moves))