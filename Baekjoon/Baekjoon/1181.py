n = int(input())

alph_lst = []

for i in range(n):
    alph_lst.append(input())

alph_lst.sort()

alph_lst.sort(key= len)


result_lst = []

for i in alph_lst:
    if i not in result_lst:
        result_lst.append(i)

for i in result_lst:
    print(i)