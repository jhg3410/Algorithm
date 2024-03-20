answer = 999999999999

def solution(n, wires):
    relations = [[False for _ in range(n)] for _ in range(n)]
    
    for wire in wires:
        x, y = map(lambda x: x - 1, wire)
        relations[x][y] = True
        relations[y][x] = True

    dfs(n, 0, relations)
    
    return answer


def dfs(n, idx, relations):
    global answer
    count = 1
    
    for i in range(n):
        if relations[idx][i]:
            relations[idx][i] = False
            relations[i][idx] = False
            count += dfs(n, i, relations)
            relations[idx][i] = True
            relations[i][idx] = True
    
    answer = min(answer, abs(n - count - count))

    return count


