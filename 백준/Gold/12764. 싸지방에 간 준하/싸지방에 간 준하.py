import heapq


def solve():
    while people:
        is_replaced = False
        start, end = heapq.heappop(people)

        for idx, end_time in enumerate(seat):
            # 기존 자리 대체
            if end_time <= start:
                seat[idx] = end
                answer[idx] += 1
                is_replaced = True
                break

        if not is_replaced:
            # 자리 추가
            seat.append(end)
            answer[len(seat) - 1] += 1


if __name__ == '__main__':
    n = int(input())
    people = []
    seat = []
    answer = [0 for _ in range(100_001)]

    for _ in range(n):
        start, end = map(int, input().split())
        heapq.heappush(people, [start, end])

    solve()
    print(len(seat))
    print(*answer[:len(seat)])
