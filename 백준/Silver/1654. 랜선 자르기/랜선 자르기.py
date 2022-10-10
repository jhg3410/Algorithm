n, m =map(int,input().split())
lst = [int(input()) for _ in range(n)]
s = sum(lst)
start = 1
end = max(lst)
while (start <= end):
    mid = (start + end) // 2
    q = sum([(i // mid) for i in lst])
    if q >= m:
        result = mid
        start = mid +1
    else:
        end = mid -1
print(result)