n = int(input())
lst = list(map(int,input().split()))

place = lst.index(-1)
right_lst = min(lst[place+1:])
left_lst = min(lst[:place])

print(right_lst+left_lst)