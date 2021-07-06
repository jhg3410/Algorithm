import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

queue = deque()

for i in range(n):
    result = input().split()

    order =  result[0]

    if order == "push": 
        queue.append(result[1])
    if order == "pop":
        if len(queue) == 0:
            print(-1)
        else: 
            print(queue.popleft())
    if order == "size":
        print(len(queue))
    if order == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    if order == "front":
        if len(queue) == 0:
            print(-1)
        else: 
            print(queue[0])
    if order == "back":
        if len(queue) == 0:
            print(-1)
        else: 
            print(queue[len(queue)-1])

