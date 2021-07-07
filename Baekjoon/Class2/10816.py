from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())
n_lst = list(map(int,input().split()))
m = int(input())
m_lst = list(map(int,input().split()))

n_lst.sort()
answer = []

for card in m_lst:
    answer.append(bisect_right(n_lst,card) - bisect_left(n_lst,card))

print(" ".join(str(a) for a in answer))