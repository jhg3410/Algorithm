import sys
input = sys.stdin.readline
n, m = map(int,input().split())

n_lst = [input().strip() for _ in range(n)]
m_lst = [input().strip() for _ in range(m)]

for i in m_lst:
    if i.isdigit():
        print(n_lst[int(i)-1])
    else:
        print(n_lst.index(i)+1)