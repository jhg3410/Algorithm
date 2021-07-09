from collections import Counter

x = int(input())
for _ in range(x):
    n = int(input())
    lst = []
    for i in range(n):
        clothes, kind = input().split()
        lst.append(kind)
    cnt = Counter(lst)
    num = 1
    for count in cnt.values():
        num = num * (count +1)
    print(num-1)