answer_list = []
input_number = 1

# nest: 중첩 수
def fill(start: int, cnt: int, nest: int):
    global input_number
    # /
    input_idx = start
    for i in range(cnt):
        if i != 0: input_idx += i + (nest + nest)
        answer_list[input_idx] = input_number
        input_number += 1
    # _
    for i in range(cnt-1):
        input_idx += 1
        answer_list[input_idx] = input_number
        input_number += 1
    # \
    for i in range(cnt-2):
        input_idx -= cnt - i + (nest + nest)
        answer_list[input_idx] = input_number
        input_number += 1

def solution(n):
    global answer_list
    answer_list = [0 for _ in range(((n + 1) * n) // 2)]
    start = 0
    nest = 0
    tmp_for_start = 4
    for k in range(n, 0, -3):
        fill(start = start, cnt = k, nest = nest)
        start += tmp_for_start
        tmp_for_start += 4
        nest += 1
    
    return answer_list