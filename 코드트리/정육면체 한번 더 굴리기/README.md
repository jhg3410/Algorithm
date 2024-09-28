# 정육면체 한번 더 굴리기

걸린 시간: 1시간 9분

`골3`

[코드트리 | 코딩테스트 준비를 위한 알고리즘 정석](https://www.codetree.ai/training-field/frequent-problems/problems/cube-rounding-again/submissions?page=2&pageSize=20)

주사위를 굴리면서 주사위에 적힌 숫자들의 변화가 관건

```python
dice = [1, 2, 6, 5, 3, 4]
# ...
if dice_dir == 0:
    new_dice = dice[1:4] + [dice[0]] + dice[4:6]
elif dice_dir == 1:
    new_dice = [dice[5]] + [dice[1]] + [dice[4]] + [dice[3]] + [dice[0]] + [dice[2]]
elif dice_dir == 2:
    new_dice = [dice[3]] + dice[0:3] + dice[4:6]
else:
    new_dice = [dice[4]] + [dice[1]] + [dice[5]] + [dice[3]] + [dice[2]] + [dice[0]]

dice = new_dice
```

이런식으로 각 기존 다이스에서 각 index 를 기준으로 변화했다.

하지만 어차피 마주보는 변의 합이 7이므로, 6개의 변을 모두 기록하고 사용하는 게 아닌, 3개의 변을 가지고 상태를 변경하면 됐다.(굳이 index 를 기준으로 안 해도 되었다.)

```python
def change_dice_number(direction):
    global dice_number
    up, front, side = dice_number
    # 오른쪽
    if direction == 0:
        n_up, n_front, n_side = 7 - side, front, up
    # 왼쪽
    elif direction == 2:
        n_up, n_front, n_side = side, front, 7 - up
    # 위쪽
    elif direction == 3:
        n_up, n_front, n_side = front, 7 - up, side
    # 아래쪽
    else:
        n_up, n_front, n_side = 7 - front, up, side

    dice_number = [abs(n_up), abs(n_front), abs(n_side)]
```