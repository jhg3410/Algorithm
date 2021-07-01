def solution(nums):
    answer = 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                temp =  nums[i]+nums[j]+nums[k]

                if find_sosu(temp):
                    answer += 1

    return answer

def find_sosu(num):
    cnt = 0
    for i in range(1,num+1):
        if num%i == 0:
            cnt += 1
    
    if cnt == 2:
        return  True


nums = [1,2,7,6,4]
print(solution(nums))
