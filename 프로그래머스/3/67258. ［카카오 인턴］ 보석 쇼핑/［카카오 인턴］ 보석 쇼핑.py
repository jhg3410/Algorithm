from collections import defaultdict

kinds = set()
gems_count = dict()

start_number = 0
end_number = 0
answer_start_number = -1
answer_end_number = -1

diff = 10 ** 10


def solution(gems):
    global kinds, start_number, end_number, answer_end_number, answer_start_number, diff
    kinds = set(gems)

    while True:
        if is_it_all():
            new_diff = end_number - start_number
            if new_diff < diff:
                answer_start_number = start_number
                answer_end_number = end_number
                diff = new_diff

            gem = gems[start_number]
            gems_count[gem] -= 1
            if gems_count[gem] == 0:
                gems_count.pop(gem)
            start_number += 1
        else:
            if end_number == len(gems):
                break
            gem = gems[end_number]
            if gem not in gems_count:
                gems_count[gem] = 1
            else:
                gems_count[gem] += 1
            end_number += 1

    return [answer_start_number + 1, answer_end_number]


def is_it_all():
    return len(gems_count) == len(kinds)


