# 바이러스 백신

걸린  시간: 46분

`골4`

[코드트리 | 코딩테스트 준비를 위한 알고리즘 정석](https://www.codetree.ai/training-field/frequent-problems/problems/vaccine-for-virus/description?page=3&pageSize=20)

간단한 백트래킹 + bfs 문제

아쉬웠던 점

- 시간을 빠르게 풀려고 하다보니 잦은 실수 발생

해설

- 백트래킹 구현 방식의 차이(조합)

  ```kotlin
  // 내 코드
  for i in range(start, hospitals_len):
    picked.append(hospitals[i])
    pick_hospital(picked=picked, start=i + 1)
    picked.pop()
  
  // 해서 코드
  if curr_idx == len(hospitals):
          return
          
  find_min_time(curr_idx + 1, cnt)
      
  selected_hos.append(hospitals[curr_idx])
  find_min_time(curr_idx + 1, cnt + 1)
  selected_hos.pop()        
  ```

요런식으로 난 반복문을 토대로 백트래킹을 돌렸고,

해설은 현재 index 선택 유무에 따른 백트래킹을 돌렸다.