import sys
input = sys.stdin.readline
n, m = map(int,input().split())

number = 1
dic_1 = {}
dic_2 = {}

for i in range(n):
    name = input().strip()
    dic_1[number] = name
    dic_2[name] = number
    number += 1

for i in range(m):
    poketmon = input().strip()
    if poketmon.isdigit():
        print(dic_1[int(poketmon)])
    else:
        print(dic_2[poketmon])
