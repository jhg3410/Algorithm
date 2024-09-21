## **산 모양 타일링**

`걸린 시간: 3시간(해설 참고)`

**LEVEL 3**

[산 모양 타일링](https://school.programmers.co.kr/learn/courses/30/lessons/258705)

`dp 문제`

`dp` 는 알고 있었지만, n 이 커질수록 중복되는 걸 제거하고 양 옆에 4가지의 모양을 붙일 수 있는 형태로 나아가서 풀려고 했다.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/b7811c85-19db-43c9-9afa-eb8a1faa1680/388ec98f-5a7c-4cf2-8d32-6b65bdd9a44b/image.png)

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

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/b7811c85-19db-43c9-9afa-eb8a1faa1680/d83afb6e-0356-4cc7-b55b-959a426a8689/image.png)

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

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/b7811c85-19db-43c9-9afa-eb8a1faa1680/5312f01b-4577-481d-8501-8a6157c1e436/image.png)

이렇게 아래의 삼각형 개수만큼 dp 를 진행하면서  `dp[n]=dp[n-1]+dp[n-2]` 를 하면 되는데, 

위에 삼각형이 있다면, `dp[n] = dp[n-1]` 을 한 번 더 해주면 된다.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/b7811c85-19db-43c9-9afa-eb8a1faa1680/c336e253-6ee1-44fd-9fe7-5974af51eef2/image.png)

위 사진처럼 이뤄진다.
