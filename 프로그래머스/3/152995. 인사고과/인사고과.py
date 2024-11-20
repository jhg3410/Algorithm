LIMIT = 100_000

def solution(scores):
    max_score2 = [0 for _ in range(LIMIT+1)]
    for score1, score2 in scores:
        if score2 > max_score2[score1]:
            max_score2[score1] = score2
            
    # 얘가 기준: 해당 idx 일 때 value 보다 크거나 같으면 인센티브를 받는다.
    min_score2 = [0 for _ in range(LIMIT+1)]
    behind_max = 0
    for i in range(LIMIT, -1, -1):
        min_score2[i] = behind_max
        behind_max = max(behind_max, max_score2[i])
        
    live_scores = []
    for score1, score2 in scores[1:]:
        if score2 >= min_score2[score1]:
            live_scores.append(score1 + score2)
            
    if scores[0][1] < min_score2[scores[0][0]]:
        return -1
    
    stand = sum(scores[0])
    answer = 0
    for score in live_scores:
        if score > stand:
            answer += 1
    return answer + 1