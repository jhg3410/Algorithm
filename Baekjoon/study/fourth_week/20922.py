n, k = map(int,input().split())
data = list(map(int,input().split()))

start = 0
end = 0
result = 0
count = [0] * 100001

while start < n:
    if count[data[start]] != k:
        count[data[start]] += 1
        start += 1
        result = max(result, start - end)

    else:
        count[data[end]] -= 1
        end += 1
        result = max(result, start - end+1)

print(result)