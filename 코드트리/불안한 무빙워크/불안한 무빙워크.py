n, k = map(int, input().split())
moving_walk = list(map(int, input().split()))
# 무빙워크에 사람들이 있는지
moving_walk_people = [False for _ in range(n * 2)]
# 사람들이 위치한 무빙워크 번호
people = []
count = 0


def run():
    rotate_moving_walk()
    move_people()
    get_on_man()


def rotate_moving_walk():
    global moving_walk, moving_walk_people
    moving_walk = [moving_walk[-1]] + moving_walk[:-1]
    moving_walk_people = [moving_walk_people[-1]] + moving_walk_people[:-1]
    get_off = -1
    for i in range(len(people)):
        people[i] += 1
        if people[i] == n - 1:
            get_off = i
    if get_off != -1:
        people.pop(get_off)
        moving_walk_people[n - 1] = False


def move_people():
    get_off = -1
    for i in range(len(people)):
        man_pos = people[i]
        if moving_walk[man_pos + 1] == 0 or moving_walk_people[man_pos + 1]:
            pass
        # 한 칸 이동
        else:
            moving_walk_people[man_pos] = False
            moving_walk_people[man_pos + 1] = True
            moving_walk[man_pos + 1] -= 1
            people[i] = man_pos + 1
            if people[i] == n - 1:
                get_off = i
    if get_off != -1:
        people.pop(get_off)
        moving_walk_people[n - 1] = False


def get_on_man():
    safety = moving_walk[0]
    if safety != 0 and not moving_walk_people[0]:
        people.append(0)
        moving_walk[0] -= 1
        moving_walk_people[0] = True


def is_end():
    return moving_walk.count(0) >= k


def print_info():
    print(f'round: {count}')
    print(moving_walk)
    print(moving_walk_people)
    print(people)
    print("------------------")


if __name__ == '__main__':
    while True:
        count += 1
        run()
        # print_info()
        if is_end():
            break
    print(count)
