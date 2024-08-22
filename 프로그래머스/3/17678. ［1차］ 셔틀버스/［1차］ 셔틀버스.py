class Time:
    hour: int
    minute: int

    def __init__(self, hour: int, minute: int):
        self.hour = hour
        self.minute = minute

    def __lt__(self, other):
        if self.hour == other.hour:
            return self.minute < other.minute
        return self.hour < other.hour

    def __le__(self, other):
        if self.hour == other.hour:
            return self.minute <= other.minute
        return self.hour <= other.hour

    def __str__(self):
        return f'{self.hour:02}:{self.minute:02}'

    def __sub__(self, other):
        if other.minute > self.minute:
            return Time(self.hour - 1, 60 - other.minute - self.minute)
        return Time(self.hour, self.minute - other.minute)


bus_start = Time(9, 0)


def get_next_time(stand: Time, minute: int):
    sum_minute = stand.minute + minute
    if sum_minute < 60:
        return Time(stand.hour, sum_minute)
    else:
        return Time(stand.hour + 1, sum_minute - 60)


def solution(n, t, m, timetable):
    times = []
    for time_str in timetable:
        hour, minute = map(int, time_str.split(":"))
        times.append(Time(hour, minute))
    times.sort()

    stand = bus_start
    bus_times = [bus_start]
    for _ in range(n - 1):
        next_time = get_next_time(stand, t)
        bus_times.append(next_time)
        stand = next_time

    take_buses = [[] for _ in range(n)]
    bus_idx = 0
    time_idx = 0
    while time_idx < len(times) and bus_idx < n:
        time = times[time_idx]
        bus = bus_times[bus_idx]
        if time <= bus:
            take_buses[bus_idx].append(time)
            if len(take_buses[bus_idx]) == m: bus_idx += 1
            time_idx += 1
        else:
            bus_idx += 1

    if len(take_buses[-1]) < m:
        return f'{bus_times[-1]}'
    else:
        return f'{take_buses[-1][-1] - Time(0, 1)}'
