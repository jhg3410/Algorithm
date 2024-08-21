stones = []
k = -1


def solution(_stones, _k):
    global stones, k

    stones, k = _stones, _k

    numbers = sorted(set(stones))
    start = 0
    end = len(numbers) - 1
    while start <= end:
        mid = (start + end) // 2
        # print(start, end, mid)
        if can_cross(numbers[mid]):
            start = mid + 1
        else:
            end = mid - 1
    return numbers[start]


def can_cross(offset: int):
    count = 0
    for stone in stones:
        if stone - offset <= 0:
            count += 1
            if count == k:
                return False
        else:
            count = 0

    return True

