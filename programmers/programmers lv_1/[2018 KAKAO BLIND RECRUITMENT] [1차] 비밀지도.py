def solution(n, arr1, arr2):
    temp1 = []
    temp2 = []
    answer = []

    a = []
    for digit1 in arr1:
        binary1 = bin(digit1).replace('b','0')
        binary1 = binary1.zfill(n)
        temp1.append(binary1[-n:])
    for digit2 in arr2:
        binary2 = bin(digit2).replace('b','0')
        binary2 = binary2.zfill(n)
        temp2.append(binary2[-n:])

    for i in range(n):
        s = ''
        for j in range(n):
            if int(temp1[i][j]) + int(temp2[i][j]) > 1:
                s += "1"
                continue
            else:
                s += str(int(temp1[i][j]) + int(temp2[i][j]))
        answer.append(s)
    for b in answer:
        b_s = ''
        for b_in in b:
            if b_in == '1':
                b_s += "#"
            else:
                b_s += " "
        a.append(b_s)


    return a

n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
print(solution(n,arr1,arr2))