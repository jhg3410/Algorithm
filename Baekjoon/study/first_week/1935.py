n = int(input())
lst = input()
a = [input() for _ in range(n)]
tmp = []
for i in lst:
    if i.isupper():
        tmp.append(int(a[ord(i) - 65]))
    else:
        num2 = tmp.pop()
        num1 = tmp.pop()
        if i == '*':
            tmp.append(num1 * num2)
        if i == '+':
            tmp.append(num1 + num2)
        if i == '-':
            tmp.append(num1 - num2)
        if i == '/':
            tmp.append(num1 / num2)

print("{:.2f}".format(tmp[0]))


