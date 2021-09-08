from itertools import permutations

n,m = map(int,input().split())

lst = [str(i) for i in range(1,n+1)]

for i in permutations(lst,m):
    print(' '.join(i))
