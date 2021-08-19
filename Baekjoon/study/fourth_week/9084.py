t = int(input())
for _ in range(t):
    n = int(input())
    wallet = list(map(int,input().split()))
    cash = int(input())
    dp = [0] * (cash+1)
    dp[0] = 1
    for coin in wallet:
        for i in range(1,cash+1):
            if i-coin >=0:
                dp[i] += dp[i-coin]
    print(dp[cash])