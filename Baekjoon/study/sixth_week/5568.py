from itertools import permutations

n = int(input())
k = int(input())
lst = [input() for _ in range(n)]

lst = list(permutations(lst,k))

result = set()

for element in lst:
    tmp = ""
    for i in range(len(element)):
        tmp += element[i]    
    result.add(int(tmp))

print(len(result))

