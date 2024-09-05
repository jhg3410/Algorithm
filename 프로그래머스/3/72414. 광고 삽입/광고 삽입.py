max_play_time = (60 * 60 * 100) - 1
# 누적합을 위해 +2
counts = [0 for _ in range(max_play_time + 2)]
# 인덱스가 max_play_time 을 참조할 수 있도록 +1
sums = [0 for _ in range(max_play_time + 1)]
play_time = -1
adv_time = -1
starts = [0]
# 시간, 사람 수
answer = (0, -1)


def solution(_play_time, _adv_time, logs):
    global play_time, adv_time, answer, sums

    play_time = change_to_second(_play_time)
    adv_time = change_to_second(_adv_time)

    for log in logs:
        start_time, end_time = log.split("-")
        start = change_to_second(start_time)
        end = change_to_second(end_time)
        starts.append(start)

        counts[start] += 1
        counts[end] -= 1

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    for i in range(len(sums)):
        sums[i] = counts[i]
    for i in range(1, len(sums)):
        sums[i] += sums[i - 1]

    for start in range(max_play_time):
        if start == 0:
            mans = sums[start + adv_time - 1]
        else:
            mans = sums[min(start + adv_time - 1, max_play_time)] - sums[start - 1]
        if mans > answer[1]:
            answer = (start, mans)

    return change_to_time(answer[0])


def change_to_second(time):
    hour, minute, second = map(int, time.split(":"))
    return second + minute * 60 + hour * 60 * 60


def change_to_time(second):
    hour = second // (60 * 60)
    second %= (60 * 60)
    minute = second // 60
    second %= 60

    return f'{hour:02}:{minute:02}:{second:02}'


if __name__ == '__main__':
    print(solution("02:03:55", "00:14:15",
                   ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
                    "01:37:44-02:02:30"]))
