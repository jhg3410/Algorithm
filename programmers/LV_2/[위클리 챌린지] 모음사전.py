import itertools

def solution(word):
    answer = 1

    alp_lst = ['A','E','I','O','U']
    all_lst = []
    for i in range(1,len(alp_lst)+1):
        all_lst += list(itertools.product(alp_lst, repeat=i))
    
    tmp = []
    for tup in all_lst:
        tmp.append(''.join(tup))
    
    tmp.sort()
    for i in tmp:
        if word == i:
            return answer
        answer+=1

print(solution("AAAAE"))