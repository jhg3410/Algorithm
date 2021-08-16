n, x = map(int,input().split())
lst = list(map(int,input().split()))

summary = 0
prefix_sum = [0]

for i in lst:
    summary += i
    prefix_sum.append(summary)

result = []

for i in range(n-x+1):
    result.append(prefix_sum[i+x] - prefix_sum[i])

if max(result) == 0:
    print("SAD")
else:
    print(max(result))
    print(result.count(max(result)))