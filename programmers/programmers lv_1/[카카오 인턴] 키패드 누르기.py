def solution(numbers, hand):
    answer = ''
    temp = []
    left = [3,0]
    right = [3,2]
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            left = [(i-1) // 3,(i % 3) -1]
        elif i in [3,6,9]:
            answer += 'R'
            right = [(i-1) // 3,(i % 3) +2]
        else:
            if i == 0:
                temp = [3,1]
            else:
                temp = [(i-1) // 3,(i % 3) -1]
            disleft = 0
            disright = 0
            for j in range(2):
                disleft += abs(left[j] - temp[j])
                disright += abs(right[j] - temp[j])

            if disleft > disright:
                answer += 'R'
                right = temp

            elif disleft < disright:
                answer += 'L'
                left = temp
                
            else:
                if hand == "left":
                    answer += 'L'
                    left = temp
                else:
                    answer += 'R'
                    right = temp

    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers,hand))