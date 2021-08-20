list_1 = list(input())
list_2 = list(input())

dp = [[0] * (len(list_2)+1)  for _ in range(len(list_1)+1)]

for i in range(1,len(list_1)+1):
    for j in range(1,len(list_2)+1):
        if list_1[i-1] == list_2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1]) 

