def solution(nums):
    answer = 0
    length = len(nums)/2
    set_num=set(nums)

    if len(set_num) <= length:
        answer = len(set_num) 
    else:
        answer = length

    return answer