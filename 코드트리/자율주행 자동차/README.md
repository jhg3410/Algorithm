# 자율주행 자동차

걸린 시간: 32분

`골5`

[코드트리 | 코딩테스트 준비를 위한 알고리즘 정석](https://www.codetree.ai/training-field/frequent-problems/problems/autonomous-driving/description?page=3&pageSize=20)

간단한 시뮬레이션

해설

- 차가 돌면서 갈 수 있는지 확인할 때, 돌린 방향을 바로 차의 방향으로 적용시켜도 괜찮음
    - 어차피 후진을 할땐 4방향 다 돌기에, 처음 방향으로 돌아와 있음
- 난 후진을 염두하고, 기존 방향을 안 바꾸고, 갈 수 있는지 확인

```python
for i in range(1, 5):
    nd = (car_d + i) % 4
    nx = car_x + dx[nd]
    ny = car_y + dy[nd]
    if not can_go(nx, ny): continue
    car_x, car_y, car_d = nx, ny, nd
    visited[nx][ny] = True
    is_moved = True
    break
```