n, length = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
correct_road_count = 0
LEFT_RAMP = -10 * 10
RIGHT_RAMP = 10 * 10
EMPTY = 0


def separate_road():
    global correct_road_count
    roads = []

    for road in board:
        roads.append(road.copy())

    for i in range(n):
        road = []
        for j in range(n):
            road.append(board[j][i])
        roads.append(road)

    for idx, road in enumerate(roads):
        ramped_road = lay_ramp(road=road)
        if not ramped_road: continue
        correct_road_count += 1


def lay_ramp(road: list[int]):
    ramped = [EMPTY for _ in range(n)]

    for idx, height in enumerate(road):
        if idx == 0:
            next_height = road[idx + 1]
            if abs(height - next_height) > 1:
                return False
            # 왼쪽에 왼쪽 경사를 넣는다.
            if height < next_height:
                if length > 1: return False
                ramped[0] = LEFT_RAMP

        elif idx == n - 1:
            pre_height = road[idx - 1]
            if abs(height - pre_height) > 1:
                return False
            # 오른쪽에 오른쪽 경사를 놓는다.
            if height < pre_height:
                if length > 1: return False
                ramped[-1] = RIGHT_RAMP

        else:
            pre_height = road[idx - 1]
            next_height = road[idx + 1]
            if abs(height - next_height) > 1:
                return False
            if abs(height - pre_height) > 1:
                return False

            # 오른쪽에 오른쪽 경사를 놓는다.
            if height < pre_height:
                # 오른쪽에 넣을 경사 공간이 없으면 끝낸다.
                if idx + length - 1 >= n:
                    return False
                right_roads = ramped[idx:idx + length]
                # 오른쪽에 이미 다른 경사가 있으면 끝낸다.
                if LEFT_RAMP in right_roads or RIGHT_RAMP in right_roads:
                    return False
                ramped[idx:idx + length] = [RIGHT_RAMP] * length
            # 왼쪽에 왼쪽 경사를 놓는다.
            if height < next_height:
                # 왼쪽에 넣을 경사 공간이 없으면 끝낸다.
                if idx - length + 1 < 0:
                    return False
                left_roads = ramped[idx - length + 1: idx + 1]
                # 왼쪽에 이미 다른 경사가 있으면 끝낸다.
                if LEFT_RAMP in left_roads or RIGHT_RAMP in left_roads:
                    return False
                ramped[idx - length + 1: idx + 1] = [LEFT_RAMP] * length

    return True


if __name__ == '__main__':
    separate_road()
    print(correct_road_count)
