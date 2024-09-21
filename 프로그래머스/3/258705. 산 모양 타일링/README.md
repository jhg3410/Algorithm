## **산 모양 타일링**

`걸린 시간: 3시간(해설 참고)`

**LEVEL 3**

[산 모양 타일링](https://school.programmers.co.kr/learn/courses/30/lessons/258705)

`dp 문제`

`dp` 는 알고 있었지만, n 이 커질수록 중복되는 걸 제거하고 양 옆에 4가지의 모양을 붙일 수 있는 형태로 나아가서 풀려고 했다.

![image](https://github.com/user-attachments/assets/e5df251f-4c33-45d9-ab60-6fe60f8b4d22)

이러한 형태였고, 이처럼 2개가 계속해서 2배씩 커지고 이게 또 n 이 증가할 수록 2배씩 커지는.. 나머지는 중복된다고 생각했다.

예를 들어, 

`n == 0` → 1

`n == 1` → 3 

`n == 2`

→ 여기서 n == 1 일때 2개가 각각 2개씩 생성하고 나머지는 모두 중복된다고 판단했다.

→ 또한 나올 수 있는 경우의 수는 이전 (n-1) 의 4배라고 생각.

→ 12(모든 경우의 수)  - (2 * 2) → 8

→ 4개는 확보하고 나머지 8개는 중복된다.

→ 4 + 8//2

→ 8

`n == 3`

→ 똑같이 32(모든 경우의 수) - (4 * 2) →24

→ 8개는 확보하고 나머지 24개는 중복된다.

→ 8 + 24//2

→ 20

이렇게 하면 위 삼각형이 없을 때의 개수를 구할 수 있겠다고 판다.

그러면 위가 있다면, ex). `n == 4, tops == [1, 1, 0, 1]`

이렇게라면

위가 마름모가 활성화 될 때마다의 경우의 수를 모두 구해주면 된다 생각했다.

![image](https://github.com/user-attachments/assets/a34504ae-af4c-48d5-9d31-05a7c4fb0065)

이렇게 `[0,0,0,0]` 일 땐, 48

`[1,0,0,0]` 일 땐 20

`[0,1,0,0]` 이면 3 * 8 = 24

해서 다 더하면 정답이라 생각했는데 140이 나옴…

- 다른 풀이

이거랑

[2024 카카오 겨울 인턴십 코딩테스트 문제해설 - tech.kakao.com](https://tech.kakao.com/posts/610)

또 하나는

```python
def solution(n, tops):
    dp = [1] * (2 * n + 2)

    for i in range(2, 2 * n + 2):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

        if i % 2 == 0 and tops[i // 2 - 1]:
            dp[i] += dp[i - 1]
    print(dp)
    return dp[-1]
```

이렇게인데, 어떤 풀이냐면

![image](https://github.com/user-attachments/assets/ccc627eb-ebac-4c96-b6dc-dc3da808975b)


이렇게 아래의 삼각형 개수만큼 dp 를 진행하면서  `dp[n]=dp[n-1]+dp[n-2]` 를 하면 되는데, 

위에 삼각형이 있다면, `dp[n] = dp[n-1]` 을 한 번 더 해주면 된다.

![image](https://github.com/user-attachments/assets/ea69c875-108f-40f6-bd2b-0008796ddae9)

위 사진처럼 이뤄진다.
