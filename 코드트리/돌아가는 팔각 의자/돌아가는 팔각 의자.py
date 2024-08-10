sits = [input() for _ in range(4)]


# 회전 방향
def rotate(sit: str, direction: int):
    if direction < 0:
        return sit[1:] + sit[0]
    else:
        return sit[-1] + sit[0:-1]


def check_rotate(number: int, direction: int):
    essential_rotate = [(number, direction)]
    current_direction = direction
    # 왼쪽
    for i in range(number, 0, -1):
        if sits[i][6] == sits[i - 1][2]:
            break
        current_direction *= -1
        essential_rotate.append((i - 1, current_direction))

    current_direction = direction
    # 오른쪽
    for i in range(number, 3, 1):
        if sits[i][2] == sits[i + 1][6]:
            break
        current_direction *= -1
        essential_rotate.append((i + 1, current_direction))

    for number, direction in essential_rotate:
        rotated = rotate(sits[number], direction)
        sits[number] = rotated


if __name__ == '__main__':
    for _ in range(int(input())):
        n, d = map(int, input().split())
        check_rotate(number=n - 1, direction=d * 100)

    answer = 0
    for idx, sit in enumerate(sits):
        answer += (2 ** idx) * int(sit[0])
    print(answer)
