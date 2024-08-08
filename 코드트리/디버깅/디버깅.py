n, m, h = map(int, input().split())
installed = [False for _ in range(h * (n - 1))]
fix = False

for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    installed[(a * (n - 1)) + b] = True


def find_all_case(limit: int, count: int, start: int):
    global fix
    if fix:
        return
    if count == limit:
        if can_fix(): fix = True
        return

    for i in range(start, len(installed)):
        if installed[i]: continue
        installed[i] = True
        find_all_case(limit=limit, count=count + 1, start=i + 1)
        installed[i] = False


def can_fix():
    for start_line in range(n):
        current_line = start_line
        for current_row in range(h):
            stand = current_row * (n - 1) + current_line
            pre = current_row * (n - 1) + current_line - 1
            if current_line == 0:
                if installed[stand]:
                    current_line += 1
            elif current_line == n - 1:
                if installed[pre]:
                    current_line -= 1
            else:
                if installed[stand]:
                    current_line += 1
                if installed[pre]:
                    current_line -= 1

        if current_line != start_line:
            return False

    return True


if __name__ == '__main__':
    answer = 0

    for line in range(0, 4):
        find_all_case(limit=line, count=0, start=0)
        if fix:
            answer = line
            break

    print(answer)
