n = int(input())
jobs = []
for start_time in range(1, n + 1):
    t, p = map(int, input().split())
    end_time = start_time + t - 1
    jobs.append([(start_time, end_time), p])

answer = 0


def check_all_case(current_time: int, current_index: int, sum_p: int):
    global answer
    if current_time > n:
        return
    if current_index == n:
        answer = max(answer, sum_p)
        return

    (start, end), money = jobs[current_index]
    if start <= current_time:
        check_all_case(current_time=current_time, current_index=current_index + 1, sum_p=sum_p)
        return
    check_all_case(current_time=end, current_index=current_index + 1, sum_p=sum_p + money)
    check_all_case(current_time=current_time, current_index=current_index + 1, sum_p=sum_p)


if __name__ == '__main__':
    check_all_case(0, 0, 0)
    print(answer)
