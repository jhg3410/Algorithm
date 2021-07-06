n , s = input().split()
n = int(n)

cnt = 0
dic = {}
for _ in range(n):
    name, answer = input().split()
    dic[name] = answer

answer = dic.get(s)

for key ,value in dic.items():
    if key == s:
        break
    else:
        if value == answer:
            cnt +=1
print(cnt)