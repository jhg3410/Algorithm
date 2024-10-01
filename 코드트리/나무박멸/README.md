# 나무박멸

걸린 시간: 1시간

`골4`

[코드트리 | 코딩테스트 준비를 위한 알고리즘 정석](https://www.codetree.ai/training-field/frequent-problems/problems/tree-kill-all/description?page=4&pageSize=5)

아쉬웠던 점

> 나무가 없는 칸에 제초제를 뿌리면 박멸되는 나무가 전혀 없는 상태로 끝이 나지만
>
- 해당 지문을 디버깅 과정에서 발견하고, 아래처럼 예외처리

```python
if trees[x][y] == 0:
    return 0
```

좋았던 점

- 아무도 못 죽일 수 있는 경우의 수도 생각해서 가장 많이 박멸하는 곳을 찾기전 초기값을 -1로 부여

```python
kill_count = -1
```