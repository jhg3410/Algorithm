n = int(input())
villages = dict()
allSum = 0
for _ in range(n):
    x, a = map(int, input().split())
    villages[x] = a
    allSum += a

leftAndMeSum = 0
for x, a in sorted(villages.items()):
    leftAndMeSum += a
    if leftAndMeSum >= allSum - leftAndMeSum:
        print(x)
        break