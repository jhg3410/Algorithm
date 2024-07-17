# 회전하는 빙하

걸린 시간: 1시간 18분

`골3`

[코드트리 | 코딩테스트 준비를 위한 알고리즘 정석](https://www.codetree.ai/training-field/frequent-problems/problems/rotating-glacier/explanation?page=2&pageSize=20)

2차원 배열 회전, bfs 문제

아쉬웠던 점

- 문제에서 회전에 관한 내용 이해에 시간이 좀 소비
- 얼음 녹이는 로직 일어나는 시점이 각각의 회전인지, 모든 회전이 끝난 후인지 헷갈려, 시간 소비

좋았던 점

- 회전 로직을 꽤나 빠르게 생각해냈다.
- 디버깅에 큰 시간을 들이지 않고 풀었다.

해설을 본 후

- 회전 로직에서 접근 방식은 동일한데 코드에서 가독성 차이가 컸다.

- 내 코드

```python
def rotate(level: int):
    for i in range(0, size, 2 ** level):
        for j in range(0, size, 2 ** level):
            # 등분한 배열 가지기
            rotate_board = [[0 for _ in range(2 ** level)] for _ in range(2 ** level)]
            for x in range(i, i + 2 ** level):
                for y in range(j, j + 2 ** level):
                    rotate_board[x - i][y - j] = board[x][y]
            # 등분한 배열 회전 후 반영
            rotated = rotate_small(rotate_board, level=level)
            for x in range(i, i + 2 ** level):
                for y in range(j, j + 2 ** level):
                    board[x][y] = rotated[x - i][y - j]

def rotate_small(rotate_board: list[list[int]], level: int):
    small_size = 2 ** level
    small_small_size = 2 ** (level - 1)
    rotated = [[0 for _ in range(small_size)] for _ in range(small_size)]
    for i in range(small_size):
        for j in range(small_size):
            # 1
            if i in range(small_small_size) and j in range(small_small_size):
                rotated[i][j + small_small_size] = rotate_board[i][j]
            # 2
            elif i in range(small_small_size) and j in range(small_small_size, small_size):
                rotated[i + small_small_size][j] = rotate_board[i][j]
            # 3
            elif i in range(small_small_size, small_size) and j in range(small_small_size, small_size):
                rotated[i][j - small_small_size] = rotate_board[i][j]
            # 4
            else:
                rotated[i - small_small_size][j] = rotate_board[i][j]
    return rotated
```

- 해설코드

```python
 (start_row, start_col)에서 half_size 크기의 격자를 
# move_dir 방향으로 이동합니다.
def move(start_row, start_col, half_size, move_dir):
    for row in range(start_row, start_row + half_size):
        for col in range(start_col, start_col + half_size):
            next_row = row + dxs[move_dir] * half_size
            next_col = col + dys[move_dir] * half_size
            
            next_grid[next_row][next_col] = grid[row][col]

def rotate(level):
    # Step1.
    # rotate 이후의 상태를 저장할
    # 배열을 0으로 초기화합니다.
    for i in range(grid_size):
        for j in range(grid_size):
            next_grid[i][j] = 0
    
    box_size, half_size = (1 << level), (1 << (level - 1))
    
    # Step2. 조건에 맞게 회전을 진행합니다.
    
    # Step2-1. 회전할 2^L * 2^L 크기 격자의 왼쪽 위 모서리 위치를 잡습니다.
    for i in range(0, grid_size, box_size):
        for j in range(0, grid_size, box_size):
            # Step2-2. 움직여야하는 2^(L - 1) * 2^(L - 1) 크기 격자의
            #          왼쪽 위 모서리를 각각 잡아
            #          알맞은 방향으로 이동시킵니다.
            move(i, j, half_size, 0)
            move(i, j + half_size, half_size, 1)
            move(i + half_size, j, half_size, 2)
            move(i + half_size, j + half_size, half_size, 3)
    
    # Step3.
    # rotate 이후의 결과를 다시
    # grid 배열로 가져옵니다.
    for i in range(grid_size):
        for j in range(grid_size):
            grid[i][j] = next_grid[i][j]
```

레벨에 따라 작은 사각형으로 자르고, 작은 사각형을 회전 시켜 다시 반영하는 로직인데,

나는 작은 사각형을 새로 만들고, 채워 넣었다면

해설은 좌표값을 기반으로 채워 넣었다.

그러다 보니 난 `rotate_small` 함수에서 인자로 받은 2차원 배열을 탐색하면서 4등분 하여 회전시켰는데,

해설은 `move` 함수가 인자로 좌표값을 받다보니, 외부에서 4등분한 좌표만 넘겨주면 됐다.