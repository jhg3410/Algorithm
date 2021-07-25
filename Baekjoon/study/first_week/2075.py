import heapq
n = int(input())
answer = []
for i in range(n):
    num_lst = list(map(int,input().split()))
    if i == 0:
        for num in num_lst:
            heapq.heappush(answer,num)
    else:
        for num in num_lst:
            if num > answer[0]:
                heapq.heappop(answer)
                heapq.heappush(answer,num)
print(answer[0])
    


