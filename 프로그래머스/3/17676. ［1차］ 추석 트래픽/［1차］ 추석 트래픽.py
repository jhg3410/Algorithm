answer = 0


def solution(lines):
    global answer
    times = []
    for line in lines:
        _, time, duration = line.split()
        end_time = change_to_ms(time=time)
        duration = float(duration.rstrip('s')) * 1000 - 1
        start_time = int(end_time - duration)
        times.append([end_time, start_time])
    while times:
        # 가장 짧은 끝 시간
        stand_time = times.pop(0)[0]
        limit = stand_time + 999

        delete_count = 0
        count = 1
        for idx, (end, start) in enumerate(times, start=1):
            if end < stand_time:
                delete_count = idx
                break
            if stand_time <= end <= limit or start <= limit:
                count += 1

        for _ in range(delete_count):
            times.pop()
        answer = max(answer, count)

    return answer


def change_to_ms(time: str):
    ms = 0
    # 01:00:04.001
    hour, minute, second = time.split(":")
    ms += int(hour) * 60 * 60 * 1000
    ms += int(minute) * 60 * 1000
    ms += float(second) * 1000
    return int(ms)


if __name__ == '__main__':
    # print(solution(lines=[
    #     "2016-09-15 01:00:04.001 2.0s",
    #     "2016-09-15 01:00:07.000 2s"
    # ]))
    # print(solution(lines=[
    #     "2016-09-15 01:00:04.002 2.0s",
    #     "2016-09-15 01:00:07.000 2s"
    # ]))
    print(solution(lines=[
        "2016-09-15 20:59:57.421 0.351s",
        "2016-09-15 20:59:58.233 1.181s",
        "2016-09-15 20:59:58.299 0.8s",
        "2016-09-15 20:59:58.688 1.041s",
        "2016-09-15 20:59:59.591 1.412s",
        "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s",
        "2016-09-15 21:00:00.748 2.31s",
        "2016-09-15 21:00:00.966 0.381s",
        "2016-09-15 21:00:02.066 2.62s"
    ]))
