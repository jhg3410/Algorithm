## **[1차] 추석 트래픽**

`걸린 시간: 50분`

LEVEL 3 

[[1차] 추석 트래픽](https://school.programmers.co.kr/learn/courses/30/lessons/17676)

`스택`

좋았던 점

- `2016-09-15 01:00:04.00` → 해당 입력에서 날짜는 뺴고 `01:00:04.00` 을 ms 단위로 변경해서 문제 해결
    - 8천만 정도지만 더 커도, 실행 시간에 영향을 주는 게 아니라 괜찮
- 언제 가장 많은 초당 처리량을 가질 수 있을까?
    - 한 입력마다 그 입력의 응답 시간을 기준으로 `1초` 뒤로 보낸 시간까지 나온 로그
    - 그래서 반복문의 기준이 오름차순인 입력을 기반으로 끝 시간이 계속되는 기준
    
    ```python
    while times:
        # 가장 짧은 끝 시간
        stand_time = times.pop(0)[0]
    ```
    
- 불필요한 연산 제거
    - 이미 로그의 응답 시간이 기준 시간보다 앞에 있다면, 더 이상 의미가 없는 로그이기에,  버리면 된다.

```python
for idx, (end, start) in enumerate(times, start=1):
	  if end < stand_time:
	      delete_count = idx
	      break
	  if stand_time <= end <= limit or start <= limit:
	      count += 1
 for _ in range(delete_count):
      times.pop()
```

다른 사람의 풀이

- 초로 계산한 다음 끝시간을 +1초를 해서 저장.
- 이후, 시작 시간을 정렬한 후(오름차순) end, start 를 계속 비교하면서 s_idx, e_idx 를 올리면서 조정(투포인터 느낌)
- 끝 시간에 +1초를 해주는 이유는 아래처럼 1초내에는 포함시켜야 하기에 첨부터 끝 시간을 1초를 늘려서 저장한 다음 start 와 비교

<img width="427" alt="image" src="https://github.com/user-attachments/assets/bf44e518-15fe-49ba-a34c-fb58d7ed06f1">


```python
def solution(lines):

    #get input
    S , E= [], [] 
    totalLines = 0 
    for line in lines:
        totalLines += 1
        type(line)
        (d,s,t) = line.split(" ")

       ##time to float
        t = float(t[0:-1])
        (hh, mm, ss) = s.split(":")
        seconds = float(hh) * 3600 + float(mm) * 60 + float(ss)

        E.append(seconds + 1)
        S.append(seconds - t + 0.001)

    #count the maxTraffic
    S.sort()

    curTraffic = 0
    maxTraffic = 0
    countE = 0
    countS = 0
    while((countE < totalLines) & (countS < totalLines)):
        if(S[countS] < E[countE]):
            curTraffic += 1
            maxTraffic = max(maxTraffic, curTraffic)
            countS += 1
        else: ## it means that a line is over.
            curTraffic -= 1
            countE += 1

    return maxTraffic

```
