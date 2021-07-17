n = int(input())

dp = [0] * 301  
s= [0] * 301
for i  in range(1,n+1):
    score = int(input())
    s[i] = score

dp[1] = s[1]
dp[2] = s[1] + s[2]
dp[3] = max(s[3] + dp[1], s[3] + s[2])


for i in range(4,n+1):  
    dp[i] = max(s[i] + dp[i-2], s[i] + s[i-1]+dp[i-3])

print(dp[n])