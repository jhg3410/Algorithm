def solution(numbers, target):
    answer = 0

    def dfs(idx,result):
        if idx == len(numbers)-1:
            if result == target:
                nonlocal answer
                answer +=1
                return
        else:
            idx += 1
            dfs(idx, result+numbers[idx])
            dfs(idx, result-numbers[idx])

    dfs(0,numbers[0])
    dfs(0,-numbers[0])
    
    return answer

print(solution([1, 1, 1, 1, 1],3))