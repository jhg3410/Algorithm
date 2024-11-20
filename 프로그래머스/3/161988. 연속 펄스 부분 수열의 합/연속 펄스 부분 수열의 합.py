def solution(sequence):
    answer = 0
    dp = [0,0]
    for idx, number in enumerate(sequence):
        offset = idx % 2 == 0
    
        dp[0] = max(0, dp[0] + number * (1 if offset else -1))
        dp[1] = max(0, dp[1] + number * (-1 if offset else 1))
        answer = max(answer, max(dp))
    return answer