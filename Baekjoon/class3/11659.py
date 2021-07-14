import sys
input = sys.stdin.readline

n, m = map(int,input().split())
lst = list(map(int,input().split()))

sum_value = 0
prefix_sum = [0]

for i in lst:
    sum_value += i
    prefix_sum.append(sum_value)

for j in range(m):
    a,b = map(int,input().split())
    print(prefix_sum[b]-prefix_sum[a-1])