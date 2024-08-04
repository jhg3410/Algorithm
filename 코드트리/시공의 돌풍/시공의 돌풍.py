WINDBLAST = -1

# 변수 선언 및 입력:
n, m, t = tuple(map(int, input().split()))

dust = [
    list(map(int, input().split()))
    for _ in range(n)
]
next_dust = [
    [0 for _ in range(m)]
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


def can_spread(x, y):
    return in_range(x, y) and dust[x][y] != WINDBLAST


# (x, y)에서 인접한 4방향으로 확산이 일어납니다.
def spread(x, y):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    curr_dust = dust[x][y]

    # 인접한 4방향으로 확산이 일어납니다.
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        # 격자 안이면서, 시공의 돌풍이 없는 곳으로만 확산이 가능합니다.
        if can_spread(nx, ny):
            next_dust[nx][ny] += curr_dust // 5
            dust[x][y] -= curr_dust // 5


def diffusion():
    # next_dust 값을 0으로 초기화합니다.
    for i in range(n):
        for j in range(m):
            next_dust[i][j] = 0

    # 시공의 돌풍을 제외한 위치에서만 확산이 일어납니다.
    for i in range(n):
        for j in range(m):
            if dust[i][j] != WINDBLAST:
                spread(i, j)

    # next_dust값을 확산 후 남은 dust에 더해줍니다.
    for i in range(n):
        for j in range(m):
            dust[i][j] += next_dust[i][j]


def counter_clockwise_roration(start_row, start_col, end_row, end_col):
    # Step1-1. 직사각형 가장 왼쪽 위 모서리 값을 temp에 저장합니다.
    temp = dust[start_row][start_col]

    # Step1-2. 직사각형 가장 위 행을 왼쪽으로 한 칸씩 shift 합니다.
    for col in range(start_col, end_col):
        dust[start_row][col] = dust[start_row][col + 1]

    # Step1-3. 직사각형 가장 오른쪽 열을 위로 한 칸씩 shift 합니다.
    for row in range(start_row, end_row):
        dust[row][end_col] = dust[row + 1][end_col]

    # Step1-4. 직사각형 가장 아래 행을 오른쪽으로 한 칸씩 shift 합니다.
    for col in range(end_col, start_col, -1):
        dust[end_row][col] = dust[end_row][col - 1]

    # Step1-5. 직사각형 가장 왼쪽 열을 아래로 한 칸씩 shift 합니다.
    for row in range(end_row, start_row, -1):
        dust[row][start_col] = dust[row - 1][start_col]

    # Step1-6. temp를 가장 왼쪽 위 모서리를 기준으로 바로 아래 칸에 넣습니다.
    dust[start_row + 1][start_col] = temp


def clockwise_rotation(start_row, start_col, end_row, end_col):

    # Step1-2. 직사각형 가장 왼쪽 열을 위로 한 칸씩 shift 합니다.
    for row in range(start_row, end_row):
        dust[row][start_col] = dust[row + 1][start_col]

    # Step1-3. 직사각형 가장 아래 행을 왼쪽으로 한 칸씩 shift 합니다.
    for col in range(start_col, end_col):
        dust[end_row][col] = dust[end_row][col + 1]

    # Step1-4. 직사각형 가장 오른쪽 열을 아래로 한 칸씩 shift 합니다.
    for row in range(end_row, start_row, -1):
        dust[row][end_col] = dust[row - 1][end_col]

    # Step1-5. 직사각형 가장 위 행을 오른쪽으로 한 칸씩 shift 합니다.
    for col in range(end_col, start_col, -1):
        dust[start_row][col] = dust[start_row][col - 1]




def cleaning():
    windblast_rows = [
        i for i in range(n)
        if dust[i][0] == WINDBLAST
    ]

    counter_clockwise_roration(0, 0, windblast_rows[0], m - 1)
    clockwise_rotation(windblast_rows[1], 0, n - 1, m - 1)

    # 돌풍 보정
    dust[windblast_rows[0]][0] = dust[windblast_rows[1]][0] = -1
    dust[windblast_rows[0]][1] = dust[windblast_rows[1]][1] = 0


def simulate():
    # 확산이 일어납니다.
    diffusion()

    # 시공의 돌풍이 청소를 진행합니다.
    cleaning()


# 총 t번 시뮬레이션을 진행합니다.
for _ in range(t):
    simulate()

ans = sum([
    dust[i][j]
    for i in range(n)
    for j in range(m)
    if dust[i][j] != WINDBLAST
])

print(ans)