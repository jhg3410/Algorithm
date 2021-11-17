def solve(num1,num2):
    for i in range(max(num1,num2),(num1*num2)+1):
        if i %num1 ==0 and i %num2  ==0:
            return i

def solution(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        answer = solve(arr[0],arr[1])
        for i in range(2,len(arr)):
            print(answer)
            answer = solve(answer,arr[i])
    
        return answer
