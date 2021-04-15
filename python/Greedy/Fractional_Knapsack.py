def Fractional_Knapsack(s):

    w = 0  # 배낭에 담긴 물건들의 무게의 합
    v = 0  # 배낭에 담긴 물건들의 가치의 합
    x = s[0]
    i = 0
    L  = []
    while w+x[1] <= c:
        L.append([x[0],x[1]])
        w = w+x[1]
        v = v+(x[1]*x[2])
        i += 1
        x = s[i]

    if (c-w) > 0 :
        L.append([x[0],c-w])
        v = v+ (c-w) * x[2]

    print(L,"총 가치는 :",v)

n, c  = map(int,input().split())  #  n = 물건의 개수  c = 용량
s = []

# s[][0] = 무게  s[][1] = 가치
for _ in range(n):
    a , w, v = input().split()   # [[주석, 50, 50000], [백금, 10, 600000] , [은, 25, 100000], [금, 15, 750000]]
    w = int(w)
    v = int(v)
    s.append([a , w, int(v/w)])

s.sort(key=lambda x: x[2],reverse=True)
print(s)

Fractional_Knapsack(s)

4 40
주석 50 50000
백금 10 600000
은 25 100000
금 15 750000