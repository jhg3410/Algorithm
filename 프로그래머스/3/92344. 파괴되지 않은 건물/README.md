## 파괴되지 않은 건물

`걸린 시간: 답지 참고`

LEVEL 3

[파괴되지 않은 건물](https://school.programmers.co.kr/learn/courses/30/lessons/92344/solution_groups?language=python3)

- 풀이를 보고,
    - 어떻게 효율성을 만족할 수 있을까?
    - skill 을 보면서 모두 미리 계산한다면 `O(n * m * k)`
    - 스킬의 모든 영역을 계산하지 않고, 누적합을 사용하면 마지막에 일괄적으로 처리가 가능
    - `n 0 0 0 -n`  을 누적합 하면 `n n n 0` 이런 식으로 특정 위치에만 `n, -n`(문제에선 degree) 를 잘 표시해주고 스킬을 모두 표시한 다음,
    - 마지막에 누적합을 해주면 해당 위치에 공격, 힐량이 나온다.
    
    [2022 카카오 신입 공채 1차 온라인 코딩테스트 for Tech developers 문제해설 - tech.kakao.com](https://tech.kakao.com/posts/488)
