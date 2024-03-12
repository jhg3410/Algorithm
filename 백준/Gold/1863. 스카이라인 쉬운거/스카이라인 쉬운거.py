n = int(input())
s = [0]
count = 0

for _ in range(n):
    x, y = map(int, input().split())
    if y > s[-1]:
        count+=1
        s.append(y)
    else:
        while y < s[-1]:
            s.pop()
        if y != s[-1]:
            s.append(y)
            count+=1

print(count)