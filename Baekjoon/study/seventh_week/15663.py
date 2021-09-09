from itertools import permutations

n, m = map(int,input().split())
temp_lst = list(map(int,input().split()))

result = []
for i in permutations(temp_lst,m):
    result.append(i)
result = sorted(set(result))

for numbers in result:
    for num in numbers:
        print(num,end=' ')
    print()
    