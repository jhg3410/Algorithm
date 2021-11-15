from itertools import permutations
import math
def solution(numbers):

    tmp = set()
    for i in range(1,len(numbers)+1):
        for i in list(permutations(numbers,i)):
            if sosu(int(''.join(i))):
                tmp.add(int(''.join(i)))       
                 
    return len(tmp)



def sosu(num):
    if num == 1 or num == 0:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i ==0:
            return False
    return True

print(solution("17"))