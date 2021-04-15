graph = [(1,2,13),(1,3,5),(2,4,9),(3,4,15),(3,5,3),(4,5,1),(4,6,7),(5,6,2)]
graph.sort(key = lambda x:x[2])

mst = []
n = 6
p= [0]

for i in range(1,n+1):
    p.append(i)


def find(u): # 부모노드를 찾아준다
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]

def union(u,v):  # 부모노드를 합쳐준다
    root1 = find(u)
    root2 = find(v)
    p[v] = root1  

tree_edge = 0
mst_cost = 0

while True:
    if tree_edge == n-1:
        break
    u,v,wt = graph.pop(0)
    if find(u) != find(v):
        union(u,v)
        mst.append((u,v))
        mst_cost += wt
        tree_edge +=1

print(mst_cost)
print(mst)