n = int(input())

cnt = 0

for _ in range(n):
    word = input()
    lst = []
    for alp in word:
        if alp in lst:
            if lst[-1] != alp:
                cnt += 1
                break
        lst.append(alp)

print(n-cnt)