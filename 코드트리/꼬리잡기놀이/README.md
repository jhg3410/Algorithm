# 꼬리잡기놀이
걸린 시간: 5시간

`골1`

[코드트리 | 코딩테스트 준비를 위한 알고리즘 정석](https://www.codetree.ai/training-field/frequent-problems/problems/tail-catch-play/description?page=4&pageSize=5)

아쉬웠던 점

- 팀에 꼬리와 머리가 연결되어 있는 경우는 고려하지 못함
- 이동 로직에서 문제가 있는 줄 알고 디버깅하다가, 공 위치 지정을 잘못해서 틀리는 걸 2시간만에 발견

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/b7811c85-19db-43c9-9afa-eb8a1faa1680/c0364fe1-35bc-4de6-bc33-487f34214ed7/image.png)

밑에서부터 위로 증가하는 줄 모르고 위에서부터 시작해서 내려오도록 로직을 짰었음…

그래서 아래의 코드처럼 방향이 `좌, 하` 이면 밑에서 부터 증가하도록 변경.

```python
ball = [(round // n) % 4, round % n]
direction, line = ball[0], ball[1] if ball[0] < 2 else n - ball[1] - 1
```

해설

- 각 팀의 레일 위치를 관리하고, 항상 머리가 처음에 들어간다. 추가로 꼬리가 머리에서 몇번째인지도 저장.
- 이렇게 해서 이동할땐 레일을 rotate 시키고, 회전 시킨걸 기반으로 board 값도 변경한다.
- 점수 획득은 레일 위치를 기반으로 순차탐색으로 찾는다.
- 공 맞아서 `reverse`할 땐 레일 위치를 머리부터 꼬리까지를 반대로 넣어주고, 길은 그저 추가한다.
    - 이러면 맨 앞이 꼬리가 되고, 차피 꼬리의 정보는 머리로부터 몇 번째인지를 가지고 있어서 이건 그대로 놔둬도 괜찮다.
    - 다시 reverse 된 레일을 기반으로 board 값 변경.