n = int(input())
honeys = list(map(int, input().split()))
answer = 0
prefixSumOfHoneys = [honeys[0]]

for i in range(1, n):
    new = prefixSumOfHoneys[i-1] + honeys[i]
    prefixSumOfHoneys.append(new)  

# 벌통 왼쪽 고정
fixSum = prefixSumOfHoneys[-1] - honeys[-1]
for i in range(1, n-1):
    varSum = prefixSumOfHoneys[i] - honeys[i]
    answer = max(answer, fixSum - honeys[i] + varSum)


fixSum = prefixSumOfHoneys[-1] - honeys[0]
# 벌통 오른쪽 고정
for i in range(1, n-1):
    varSum = prefixSumOfHoneys[-1] - prefixSumOfHoneys[i]
    answer = max(answer, fixSum - honeys[i] + varSum)


# 벌통이 중간
pickMiddle = max(honeys[1:n])
answer = max(answer, prefixSumOfHoneys[-1] + pickMiddle - honeys[0] - honeys[-1])

print(answer)