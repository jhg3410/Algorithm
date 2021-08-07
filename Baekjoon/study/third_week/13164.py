n, k = map(int,input().split())
lst = list(map(int,input().split()))

diff_lst = []

for i in range(n-1):
    diff_lst.append(lst[i+1]  - lst[i])

diff_lst.sort()

print(sum(diff_lst[:n-k]))