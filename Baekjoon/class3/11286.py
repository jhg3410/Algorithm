import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []
lst = []
for i in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(heap,(x,x))
    elif x < 0:
        heapq.heappush(heap,(-x,x))
    elif x == 0 and heap:
        print(heapq.heappop(heap)[1])
    elif x == 0 and not heap:
        print(0)
