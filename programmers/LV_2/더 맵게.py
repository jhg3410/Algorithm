import heapq
def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    try:
        while True:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            heapq.heappush(scoville,a + (b*2))
            cnt += 1
            if scoville[0] >= K:
                return cnt
    except:
        return -1    
    
    

scoville =[1, 2, 3, 9, 10, 12]	
solution(scoville,7)

