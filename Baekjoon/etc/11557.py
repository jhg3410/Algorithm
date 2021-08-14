t = int(input())
for _ in range(t):
    dic = {}
    n = int(input())
    for i in range(n):
        name, num = input().split()
        num = int(num)
        dic[name] = num
    print(max(dic.keys(), key = (lambda k : dic[k])))
    
