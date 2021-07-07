from bisect import bisect_left, bisect_right

n = int(input())
n_lst = list(map(int,input().split()))

m = int(input())
m_lst = list(map(int,input().split()))

n_lst.sort()
for a in m_lst:
    if (bisect_right(n_lst,a) - bisect_left(n_lst,a)) > 0 :
        print("1")
    else:
        print("0")