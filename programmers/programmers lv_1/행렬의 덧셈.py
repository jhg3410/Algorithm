def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr1[0])):
            tmp.append(arr1[i][j] + arr2[i][j])
        answer.append(tmp)
    return answer

arr1 = [[1,2,3],[2,3,4]]
arr2 = [[3,4,3],[2,5,6]]
print(solution(arr1,arr2))