import sys
input = sys.stdin.readline
n = int(input())
n_lst = list(map(int,input().split()))

m = int(input())
m_lst = list(map(int,input().split()))

result_lst = []

for i in m_lst:
    result_lst.append(n_lst.count(i))   

for i in result_lst:
    print(i,end= " ")

