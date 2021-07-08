import sys
input = sys.stdin.readline

m = int(input())    
S = set()

for _ in range(m):
    a = input().strip().split()
    if len(a) == 1:
        inp = a[0]
        if inp == 'all':
            S = set(i for i in range(1,21))
        elif inp == 'empty':
            S = set()
    else:
        inp,x  = a[0], int(a[1])
        if inp == 'add':
            S.add(x)
        elif inp == 'remove':
            S.discard(x)
        elif inp == 'check':
            print(1 if x in S else 0)
        elif inp == 'toggle':
            S.discard(x) if x in S else S.add(x)