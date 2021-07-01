def solution(answers):
    answer = []
    first_man = [1,2,3,4,5]
    second_man = [2,1,2,3,2,4,2,5]
    third_man = [3,3,1,1,2,2,4,4,5,5]    
    
    first_cnt = 0
    second_cnt = 0
    third_cnt = 0
    lst = []
    for i in range(len(answers)):
        if answers[i] == first_man[i%5]:
            first_cnt+=1
        if answers[i] == second_man[i%8]:
            second_cnt+=1
        if answers[i] == third_man[i%10]:
            third_cnt+=1
    lst.append(first_cnt)
    lst.append(second_cnt)
    lst.append(third_cnt)
    a = max(lst)
    for j,k in enumerate(lst):
        if k == a:
            answer.append(j+1)

    return answer

answers = [1,3,2,4,2]
print(solution(answers))