import sys 
input = sys.stdin.readline

n, m = map(int,input().split())
a_lst = list(map(int,input().split()))
b_lst = list(map(int,input().split()))

a_lst.extend(b_lst)
a_lst.sort()

print(*a_lst)