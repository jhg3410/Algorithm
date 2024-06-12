def solution(data, col, row_begin, row_end):
    # 정렬
    data.sort(key=lambda x: (x[col - 1], -x[0]))

    # 합 정의
    s = []

    for idx, row in enumerate(data):
        s.append(sum(map(lambda x: x % (idx + 1), row)))

    # 해시값 반환
    hash_value = 0
    for r_s in s[row_begin - 1: row_end]:
        hash_value = xor(r_s, hash_value)

    return hash_value


def xor(a: int, b: int):
    b_a = ""
    b_b = ""

    while a != 0:
        b_a = str(a % 2) + b_a
        a //= 2

    while b != 0:
        b_b = str(b % 2) + b_b
        b //= 2

    while len(b_a) != len(b_b):
        if len(b_a) < len(b_b):
            b_a = "0" + b_a
        else:
            b_b = "0" + b_b

    result = 0
    for idx, (a_i, b_i) in enumerate(zip(b_a, b_b)):
        result += (2 ** (len(b_a) - idx - 1)) * (a_i != b_i)

    return result


if __name__ == '__main__':
    print(solution([[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3))
