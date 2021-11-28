from collections import deque

def solution(N, road, K):
    node = {}
    for i,j,score in road:
        node[i] = node.get(i,[]) + [(j,score)]
        node[j] = node.get(j,[]) + [(i,score)]
    dist = [float('inf') if i != 1 else 0  for i in range(N+1)] 

    queue = deque([1])
    while queue:
        start = queue.popleft()
        for end,score in node[start]:
            if dist[end] > dist[start] + score :
                dist[end] = dist[start] + score
                queue.append(end)

    answer = len([True for i in range(1,N+1) if dist[i] <=K])
    return answer

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]	
K = 3
print(solution(N,road,K)) 