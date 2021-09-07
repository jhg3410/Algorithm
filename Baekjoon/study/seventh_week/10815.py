def binary_search(array,target,start,end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array,target,start, mid - 1)
    else:
        return binary_search(array,target,mid+1, end)

n = int(input())
n_lst = list(map(int,input().split()))

n_lst.sort()

m = int(input())
m_lst = list(map(int,input().split()))


for i in range(m):
    if binary_search(n_lst, m_lst[i], 0, n - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')
