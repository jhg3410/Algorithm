n, m = map(int,input().split())
lst = list(map(int,input().split()))

start = 0
end = max(lst)
result = 0

while (start <= end):
    mid = (start + end) // 2
    s = sum([i - mid for i in lst if i > mid])
    if s >= m:
        result = mid
        start = mid +1
    else:
        end = mid - 1

print(result)