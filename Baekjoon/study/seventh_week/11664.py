from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

def count_by_range(a,left_value, right_value):
    right_value = bisect_right(a,right_value)
    left_value = bisect_left(a,left_value)
    return right_value-left_value

n,m = map(int,input().split())
dot_lst = list(map(int,input().split()))
dot_lst.sort()

for _ in range(m):
    start, end = map(int,input().split())
    print(count_by_range(dot_lst,start,end))