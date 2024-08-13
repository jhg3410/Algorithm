걸린 시간: 37분

골4

[코드트리 | 코딩테스트 준비를 위한 알고리즘 정석](https://www.codetree.ai/training-field/frequent-problems/problems/cube-rounding/description?page=4&pageSize=20)

정육면체(주사위)를 돌리는 로직을 생각해내는 시뮬레이션

좋았던 점

- 주사위의 6면을 임의의 숫자로 지정을 해준 뒤,

  ![image.png](https://github.com/user-attachments/assets/91d56cc2-ed9f-4d85-851c-81c65575597a)

    - 이동할 땐 내부의 값을 변경하는 방식
    - 이동할 때 어떻게 내부의 값을 바꿀 지는 정적으로 선언

    ```python
    dice_rotate_helper = [
        # 동쪽
        [5, 1, 4, 3, 0, 2],
        # 서쪽
        [4, 1, 5, 3, 2, 0],
        # 북쪽
        [3, 0, 1, 2, 4, 5],
        # 남쪽
        [1, 2, 3, 0, 4, 5]
    ]
    ```

    - 동쪽일 땐 0 자리에 5가 들어가고, 2 자리에 4가 들어가고… 방식

해설

- 위-아래, 오른쪽 - 왼쪽 처럼 서로 마주보는 변의 합은 `7`이란 걸 활용
    - 그래서 결국 3면만 알고 있으면 나머지 3면은 유추가 가능
    - 그렇게 아래처럼 4방향 이동할 때의 방식을 일반화해서 해결

  ![image.png](https://github.com/user-attachments/assets/acb8cfdf-f941-41fa-89dc-b564498eada5)

- 또한 문제 해결할 때 실질적으로 변경이 필요한 곳은 아래(칸과 맞닿는)면이 유일하다