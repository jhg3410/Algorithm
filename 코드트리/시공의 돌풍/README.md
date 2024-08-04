# 시공의 돌풍

걸린 시간: 40분

`골5`

[코드트리 | 코딩테스트 준비를 위한 알고리즘 정석](https://www.codetree.ai/training-field/frequent-problems/problems/heros-of-storm/description?page=3&pageSize=20)

간단한 dx, dy 시뮬레이션

좋았던 점

- 토네이도의 이동 좌표를 방향을 가지고 조절
    - 방향 변경의 조건은 격자 범위를 벗어나는 걸로

해설

- 해설은 아래처럼 토네이도 이동 좌표를 다음과 같이 구간별로 나눠서 진행
    - 직관적이긴 하지만, 코드 짤 때 쉽게 실수할 수도

```python
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
```