import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)
t = []
p = []
for _ in range(n):
    a, b = map(int,input().split())
    t.append(a)
    p.append(b)

tmp = 0
for i in range(n):
    tmp = max(dp[i],tmp)
    if (i + t[i]) > n:
        continue
    dp[i+t[i]] = max(p[i]+tmp, dp[i+t[i]])

print(max(dp))