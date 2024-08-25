key = []
lock = []
key_values = []
lock_values = []
n, m = -1, -1
# 미리 회전시켜놓자
rotated_keys = [[] for _ in range(4)]
lock_count = 0


def solution(_key, _lock):
    global key, lock, n, m, lock_count
    key, lock = _key, _lock
    n, m = len(lock), len(key)
    # 키 1값들 구하기
    for x in range(m):
        for y in range(m):
            if key[x][y] == 1:
                key_values.append([x, y])

    # 회전 시킨 키 위치들 구하기 (오른쪽으로 90도)
    rotated_keys[0] = key_values
    for i in range(1, 4):
        for key_x, key_y in rotated_keys[i - 1]:
            rotated_keys[i].append([key_y, m - 1 - key_x])

    # 자물솨 1값들 구하기
    for x in range(n):
        for y in range(n):
            if lock[x][y] == 0:
                lock_count += 1
                lock_values.append([x, y])

    if len(lock_values) == 0: return True

    for i in range(4):
        for key_x, key_y in rotated_keys[i]:
            if is_fit(key_pos=[key_x, key_y], lock_pos=[lock_values[0][0], lock_values[0][1]], rotate_count=i):
                return True

    return False


def is_fit(key_pos: list, lock_pos: list, rotate_count: int):
    # print(key_pos, lock_pos, rotate_count, rotated_keys[rotate_count])
    dis_x = lock_pos[0] - key_pos[0]
    dis_y = lock_pos[1] - key_pos[1]

    count = 0
    for key_x, key_y in rotated_keys[rotate_count]:
        # print(key_x + dis_x, key_y + dis_y)
        nx, ny = key_x + dis_x, key_y + dis_y
        if [nx, ny] in lock_values:
            count += 1
            continue
        if nx not in range(n) or ny not in range(n): continue
        return False

    return count == lock_count


if __name__ == '__main__':
    # print(solution(_key=[[0, 0, 0], [0, 1, 1], [1, 0, 0]], _lock=[[1, 1, 1], [1, 1, 1], [0, 0, 1]]))
    print(solution(_key=[[1]], _lock=[[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
