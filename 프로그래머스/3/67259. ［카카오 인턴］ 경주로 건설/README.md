## 경주로 건설

`걸린 시간: 1시간 30분`

LEVEL3

좋았던 점

- 3차원 배열을 bfs 로 항상 최솟값만 탐색하도록 구상
- 3차원은 `cost_board[x][y][수직, 수평]` 으로 수직과 수평을 분리해서 cost 를 가져감

아쉬웠던 점

- 첨엔 2차원으로 접근 단순히 현재값이 이미 저장된 값보다 크면 탐색을 중지 시켰는데, 수직, 수평에 따라 값이 커도 더 작아질 수 있는 걸 생각 못 함

또 다른 풀이

- visited 를 아래처럼 dict 로 넣고 각 방향마다 체크한다
    
    ```python
    visit = {(0,0,0):0, (0,0,1):0, (0,0,2):0, (0,0,3):0}
    ```
    
    - 4방향이 아닌, `수직 수평` 두 개로 놓고 해도 된다.
