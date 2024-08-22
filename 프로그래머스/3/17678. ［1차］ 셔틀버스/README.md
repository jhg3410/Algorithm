## 셔틀버스
`걸린 시간: 1시간 10분`

LEVEL 3

[셔틀버스](https://school.programmers.co.kr/learn/courses/30/lessons/17678)

좋았던 점

- Time 이란 클래스(`hour: int, minute: int`) 를 선언해서 시간을 다룸
- 가장 늦게 도착하는 시간을 구하는 방법을 빠르게 구상

아쉬운 점

- `class` 선언과 내부 오버라이딩 메서드(`le`, `str`, `lt`, `sub`)를 검색해서 알아냄,,
- 0 을 채우는 방식 `rjust(width, fillchar)`, `“number”:02`

다른 분의 풀이

- 시간 * 60 + 분 으로 시간을 분으로 모두 바꿔서 다루면 편함
    
    ```python
    timetable=[int(i[:2])*60+int(i[3:]) for i in timetable]
    bustable=[9*60+t*i for i in range(n)]
    ```
