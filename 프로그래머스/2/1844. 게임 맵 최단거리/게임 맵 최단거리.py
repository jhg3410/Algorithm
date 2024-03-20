from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def solution(maps):
    return bfs(len(maps), len(maps[0]), maps) 
    

def bfs(n,m,maps):
    count = 0
    queue = deque()
    queue.append([0,0,1])
    
    while(queue):
        x, y, count = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx not in range(n) or ny not in range(m): continue
            if maps[nx][ny] == 0: continue
            queue.append([nx, ny, count+1])
            maps[nx][ny] = 0
            if nx == n-1 and ny == m-1: 
                return count+1
                
            
    return -1


