import heapq
import sys
input = sys.stdin.readline

n = int(input())
people = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
seat = []
possible_index = []
answer = [0] * (n + 1)

for start, end in people:
    # 시간이 다 된 자리는 뺀다.
    while seat and seat[0][0] <= start:
        end_time, idx = heapq.heappop(seat)
        heapq.heappush(possible_index, idx)

    # 사람을 자리에 넣는 부분
    if possible_index:
        idx = heapq.heappop(possible_index)
    else:
        idx = len(seat)

    heapq.heappush(seat, [end, idx])
    answer[idx] += 1

count_seat = answer.index(0)
print(count_seat)
print(' '.join(map(str, answer[:count_seat])))
