n = int(input())
lst = list(map(int,input().split()))

summary = 0
prefix_sum = [0]
for i in lst:
    summary += i
    prefix_sum.append(summary)

lst_sum = prefix_sum[-1]

result = 0

# 벌통이 맨 오른쪽이면 하나의 벌은 맨 왼쪽 고정
for i in range(1,n-1):
    prefix = prefix_sum[n] - prefix_sum[i+1]
    result = max(result,lst_sum - lst[0] - lst[i] + prefix)

# 벌통이 맨 왼쪽이면 하나의 벌은 맨 오른쪽 고정
for i in range(1,n-1):
    prefix = prefix_sum[i] - prefix_sum[0]
    result = max(result, lst_sum - lst[-1] - lst[i] + prefix)

# 벌통이 끝에 있지 않다면 벌은 무조건 왼쪽 끝과 오른쪽 끝
for i in range(1,n-1):
    # prefix_left = prefix_sum[i+1] - prefix_sum[1]
    # prefix_right = prefix_sum[n-1] - prefix_sum[i]
    # result = max(result, prefix_left + prefix_right)
    result = max(result ,lst_sum - lst[0]- lst[-1]+ lst[i])

print(result)