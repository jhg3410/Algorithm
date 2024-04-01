from collections import defaultdict


def solution(k, tangerines):
    limit = k

    tan_cnt = defaultdict(int)

    for tangerine in tangerines:
        tan_cnt[tangerine] += 1
    sorted_tan_cnt = {x: y for x, y in sorted(tan_cnt.items(), key=lambda x: x[1], reverse=True)}
    for idx, tan_cnt in enumerate(sorted_tan_cnt.values()):
        limit -= tan_cnt
        if limit <= 0:
            return idx + 1