def solution(s):
    answer = 1
    dp = [[False for _ in range(len(s))] for _ in range(len(s))]
    
    for i in range(len(s)):
        dp[i][i] = True
        
    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            answer = 2
    
    for length in range(3, len(s)+1):
        for i in range(0, len(s) - length + 1):
            front = i
            end = i+length-1
            if s[front] == s[end] and dp[front+1][end-1]:
                dp[front][end] = True
                answer = max(answer, length)
    
    return answer
