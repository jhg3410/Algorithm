answer = 0
def solution(k, dungeons):
    findDungeons(k, dungeons, [])
    return answer

def findDungeons(k, dungeons, visited):
    global answer
    for i in range(len(dungeons)):
        if i not in visited and k - dungeons[i][0] >= 0:
            visited.append(i)
            findDungeons(k - dungeons[i][1], dungeons, visited)
            visited.pop()
        answer = max(answer, len(visited))
    
    