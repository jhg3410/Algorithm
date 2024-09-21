def solution(n, tops):
    a = [0 for _ in range(n + 1)]
    b = [0 for _ in range(n + 1)]
    a[0] = 1

    for number, top in enumerate(tops, start=1):
        if top == 1:
            a[number] = 3 * a[number - 1] + 2 * b[number - 1]
            b[number] = a[number - 1] + b[number - 1]
        else:
            a[number] = 2 * a[number - 1] + b[number - 1]
            b[number] = a[number - 1] + b[number - 1]

        a[number] %= 10007
        b[number] %= 10007

    return (a[n] + b[n]) % 10007


if __name__ == '__main__':
    print(solution(n=4, tops=[1, 1, 0, 1]))
