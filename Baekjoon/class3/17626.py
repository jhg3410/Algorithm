import math
import sys
input = sys.stdin.readline
n = int(input())

dp = [0] *(n+1)
dp[0]= 0
dp[1] = 1

for i in range(2,n+1):
    if math.sqrt(i).is_integer():
        dp[i] = 1
    else:
        dp[i] = i
#  이해가 안되면 직접 노트에 1부터 9까지해서 각 조합을 만들어 보면 
# ex) 7 = 2**2 + 1**1 + 1**1 + 1**1   dp[7 - 1] = dp[6]이 이미 앞에 3개의 덧셈을 가지고 있어서 
# dp[1] + dp [7 - 1] 하면 2가 나온다 dp[1] = 1**1이라 
for i in range(2,n+1):
    for j in range(1,int(math.sqrt(i))+1):
        dp[i] = min(dp[i], dp[j*j] + dp[i-j*j])

print(dp[n])

