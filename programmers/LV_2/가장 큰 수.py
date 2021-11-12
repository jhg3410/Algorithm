def solution(numbers):
    lst = list(map(str,numbers))
    lst.sort(key= lambda x:x*3 ,reverse= True)
    if sum(list(map(int,lst))) == 0:
        return '0'
    return ''.join(lst)

print(solution([0, 1, 0]))