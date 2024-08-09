n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

selected = []
min_answer = 10 ** 10
max_answer = -10 ** 10


def update_answer(result: int):
    global min_answer, max_answer
    min_answer = min(min_answer, result)
    max_answer = max(max_answer, result)


def check_all_case():
    if len(selected) == n - 1:
        result = calculate()
        update_answer(result=result)
        return

    for i in range(3):
        if operators[i] == 0: continue
        operators[i] -= 1
        selected.append(i)
        check_all_case()
        operators[i] += 1
        selected.pop()


def calculate():
    result = numbers[0]
    for idx, number in enumerate(numbers):
        if idx == 0:
            continue
        # 뎃셈
        if selected[idx - 1] == 0:
            result += numbers[idx]
        # 뺄셈
        elif selected[idx - 1] == 1:
            result -= numbers[idx]
        else:
            result *= numbers[idx]
    return result


if __name__ == '__main__':
    check_all_case()
    print(min_answer, max_answer)
