# 2차원 테트리스

걸린 시간: 2시간 33분

`골2`

[코드트리 | 코딩테스트 준비를 위한 알고리즘 정석](https://www.codetree.ai/training-field/frequent-problems/problems/tetris-2d/description?page=2&pageSize=20)

좌표값 설정(이동)이 꽤나 복잡했던 시뮬레이션

좋았던 점

- 노랑, 빨강 보드를 같이 고려해서 코드를 짠 점
- 연한 영역을 따로 처리하지 않고, 보드의 크기를 2씩 증가시켜서 처리한 점

아쉬웠던 점

- 문제 설명에서 연한 보드 처리 과정이 이해되기까지 시간이 좀 걸림
- 좌표값을 너무 이리저리 가지고 하다보니 중간 중간 뇌정지가 옴

해설을 읽고

- 노란색 보드를 기준으로 모든 함수가 되어있고,
    - 빨간색 보드는 90도 시계방항향으로 회전하면 노란색 보드랑 똑같이 가져갈 수 있다.
    - 여기서 입력받은 타입, 좌표만 조정해주면 됨
- 보드를 3차원으로 board[보드 타입][행][열] 이렇게 가져감 - 위처럼 할 수 있어야 가능
- `python` 에서도 all, any 가 가능하다니.. 아래처럼 내부에 boolean 리스트로 체크

```python
def all_filled(b_num, row):
	return all([
	    board[b_num][row][col] == 1
	    for col in range(m)
	])

def block_exist(b_num, row):
	return any([
	    board[b_num][row][col] == 1
	    for col in range(m)
	])
```