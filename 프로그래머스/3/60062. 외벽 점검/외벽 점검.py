from itertools import permutations

n, weaks, dists = 0, [], []
weaks_count = -1
friend_count = -1
answer = 10 ** 10
real_weak = []


def solution(_n, _weak, _dist):
    global n, weaks, dists, weaks_count, friend_count, real_weak, answer
    n, weaks, dists = _n, _weak.copy(), sorted(_dist, reverse=True)

    real_weak = _weak.copy()
    weaks_count = len(weaks)
    friend_count = len(dists)

    for weak in _weak:
        weaks.append(weak + n)

    for i in range(1, len(dists) + 1):
        for case in get_all_case([], i, [False] * len(dists)):
            if check(case):
                return i

    return -1


def get_all_case(li, count, used):
    if len(li) == count:
        return [li.copy()]

    tmp = []
    for i, dist in enumerate(dists):
        if used[i]: continue
        li.append(dist)
        used[i] = True
        tmp.extend(get_all_case(li, count, used))
        li.pop()
        used[i] = False

    return tmp


def check(case):
    global answer
    for i in range(weaks_count):
        new_weaks = weaks[i: i + weaks_count]
        idx = 0
        for dist in case:
            bound = new_weaks[idx] + dist
            while bound >= new_weaks[idx]:
                idx += 1
                if idx == weaks_count:
                    return True
    return False


if __name__ == '__main__':
    print(solution(_n=16, _weak=[1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 14, 15], _dist=[4, 2, 1, 1]))
