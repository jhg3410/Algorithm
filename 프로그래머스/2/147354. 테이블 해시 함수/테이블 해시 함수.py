def solution(data, col, row_begin, row_end):
    answer = 0

    # 정렬
    data.sort(key=lambda x: (x[col - 1], -x[0]))

    # 합 정의
    s = []

    for idx, row in enumerate(data):
        s.append(sum(map(lambda x: x % (idx + 1), row)))

    # 해시값 반환
    hash_value = 0
    for r_s in s[row_begin - 1: row_end]:
        hash_value = r_s ^ hash_value

    return hash_value
