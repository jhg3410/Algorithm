## 광고 삽입

`걸린 시간: 3시간(질문하기 참고)`

LEVEL 3

[광고 삽입](https://school.programmers.co.kr/learn/courses/30/lessons/72414)

누적합 문제

좋았던 점

- 누적합 생각

아쉬웠던 점

- 재생이 종료된 시각을 포함하도록 계산

> `동영상 재생시간 = 재생이 종료된 시각 - 재생이 시작된 시각`(예를 들어, `00시 00분 01초`부터 `00시 00분 10초`까지 동영상이 재생되었다면, 동영상 재생시간은 `9초` 입니다.) [↩](https://school.programmers.co.kr/learn/courses/30/lessons/72414#fnref1)
> 

모든 영상에 대해 시작 시간과 끝 시간이 주어진다면: 끝 시간은 실제 재생 시간에 포함되지 않는다.

그래서 광고의 재생시간이 `14:15` 초 이고 시작 시간이 `00:00` 이라면 `00:00` 부터 사용자들은 집계되지만, `14:15` 초의 사용자는 집계되지 않는다.

`14:15` 까지 집계되면 재생 시간이 `14:16` 초가 된다.

다른 분의 풀이

- 누적합 방식
    - 내 방식
        
        ```python
        for log in logs:
            start_time, end_time = log.split("-")
            start = change_to_second(start_time)
            end = change_to_second(end_time)
            starts.append(start)
        
            counts[start] += 1
            counts[end] -= 1
        
        for i in range(1, len(counts)):
            counts[i] += counts[i - 1]
        
        for i in range(1, len(counts)):
            counts[i] += counts[i - 1]
        
        ```
        
        - 로그를 하나씩 보면서 시작 지점 +1 마지막 지점 -1 을 한 뒤 앞에서 부터 다 더해주면 각 시간마다의 사용자가 나옴
        - 여기서 다시 첨부터 끝까지 앞에껄 더하면 누적합이 생성
    - 다른 분
        
        ```python
        for l in logs:
              st, en = map(s2i, l.split('-'))
              d[st] += 1
              d[en] -= 1
        for i in range(1, 360001):
            d[i] += d[i-1]
        mxval, mxtime = sum(d[:at]), 0
        curval = mxval
        for i in range(1, 360001-at):
            curval = curval - d[i-1] + d[i+at-1]
            if curval > mxval:
                mxval = curval
                mxtime = i
        ```
        
        - 누적합을 생성하지 않고, 각 시간마다의 사용자만 모두 구한 뒤
        - 처음 0 부터 광고시간까지의 합을 구하고
        - 그다음 순차탐색하면서 이전을 뺴고 이후를 더해주는 방식으로 접근
