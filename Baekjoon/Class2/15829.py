n = int(input())
s = input()
sum = 0
a = 0
for i in s:
    sum += (ord(i)-96) *(31**a)
    a+= 1

print(sum% 1234567891)