def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        tmp = []
        for i in tree:
            if i in skill:
                tmp.append(skill.index(i)+1)
        sort_tmp = sorted(tmp)
        if sort_tmp != tmp:
            continue
        a = True
        for i in range(len(tmp)):
            if tmp[i] != i+1:
                a = False
                continue
        if a == False:
            continue
        answer+=1
    
    return answer

skill = 'CBD'
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]	
print(solution(skill,skill_trees))