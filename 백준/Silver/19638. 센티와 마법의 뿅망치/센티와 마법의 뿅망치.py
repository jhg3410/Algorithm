import heapq

def solution(n,h,t,giant_li):
    cnt = 0
    for _ in range(t):
        tallest = -giant_li[0]
        if h > tallest or tallest == 1:
            break

        heapq.heappush(giant_li,-(-heapq.heappop(giant_li)//2))
        cnt += 1
    
    if h <= -giant_li[0]:
        return 'NO', -giant_li[0]
    else:
        return 'YES', cnt

n, h, t = map(int,input().split())
giant_li = []
for _ in range(n):
    tall = int(input())
    heapq.heappush(giant_li,-tall)

answers = solution(n,h,t,giant_li)
for answer in answers:
    print(answer)