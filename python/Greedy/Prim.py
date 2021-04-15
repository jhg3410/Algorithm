INF = 999
adj_mat = [[0, 29, INF, INF, INF, 10, INF],
           [29, 0, 16, INF, INF, INF, 15],
           [INF, 16, 0, 12, INF, INF, INF],
           [INF, INF, 12, 0, 22, INF, 18],
           [INF, INF, INF, 22, 0, 27, 25],
           [10, INF, INF, INF, 27, 0, INF],
           [INF, 15, INF, 18, 25, INF, 0]]

node_num = len(adj_mat)
visited = [False] * node_num
distances = [INF] * node_num


# 포함되지않은 노드중에서 가장 짧은 노드 찾기(간선연결이 없으면 INF라 불포함되어 간선이 연결되어있는 노드만 참고된다)
def get_min_node(node_num):
    for i in range(node_num):
        if not visited[i]:
            v = i
            break
    for i in range(node_num):
        if not visited[i] and distances[i] < distances[v]:
            v = i
    return v



def prim(start, node_num):
    for i in range(node_num):
        visited[i] = False
        distances[i] = INF

    distances[start] = 0 # 시작노드의 distance의 값은 0
    for i in range(node_num):
        node = get_min_node(node_num)
        visited[node] = True # 방문처리
        print(node,end= " ")
        for j in range(node_num): 
            if adj_mat[node][j] != INF: # 연결되어있으면 INF가 아니다
                if not visited[j] and adj_mat[node][j] < distances[j]: # 연결되어있다는 것을 나타냄
                    distances[j] = adj_mat[node][j] # distance 새로고침

# 만약 0 ,5 에서 찾아야한다면 이미 0에서 1 은 새로고침되어있기에 5노드에서 연결되어있는 노드의 distance만 새로고침하면 get_min_node에서
# 새로고침된 노드중에서 가장 짧은 노드를 찾아준다
prim(0, node_num)
print("distances: ", distances)
print("minimum cost: ", sum(distances))