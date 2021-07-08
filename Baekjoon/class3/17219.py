import sys
input = sys.stdin.readline
n, m = map(int,input().split())
n_lst = {}

for i in range(n):
    site, password = input().split()
    n_lst[site] = password

for j in range(m):
    print(n_lst[input().strip()])



            