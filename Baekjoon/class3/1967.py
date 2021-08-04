import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n = int(input())

def dfs(start, tree, weight_lst):
    for node, w in tree[start]:
        if weight_lst[node] == 0:
            weight_lst[node] = weight_lst[start] + w
            dfs(node,tree,weight_lst)

tree = [[] for _ in range(n+1)]

weight_lst1 = [0 for _ in range(n+1)]   
weight_lst2 = [0 for _ in range(n+1)]
for _ in range(n-1):
    p,c,w = map(int,input().split())
    tree[p].append([c,w])
    tree[c].append([p,w])

dfs(1,tree,weight_lst1)
weight_lst1[1] = 0
long_node = weight_lst1.index(max(weight_lst1))
dfs(long_node,tree,weight_lst2)
weight_lst2[long_node] = 0
print(max(weight_lst2))