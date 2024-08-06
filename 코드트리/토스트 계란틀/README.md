# 토스트 계란틀

걸린 시간: 20분

`골5`

[코드트리 | 코딩테스트 준비를 위한 알고리즘 정석](https://www.codetree.ai/training-field/frequent-problems/problems/toast-eggmold/description?page=3&pageSize=20)

매우 간단한 bfs 문제

해설

- 난 `next_board` 를 만들어 bfs 에서 나온 결과를 바로 반영하지 않도록 해서 해결
- 하지만 바로 반영해도, `visited` 처리로 이전에 수행된 격자는 `continue` 처리를 해줘서 딱히 의미가 없었던..