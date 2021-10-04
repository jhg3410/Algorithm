n = int(input())

i = 1 
tmp = 1
if n == 1:
    print(i)
else:
    while True:
        tmp += (i*6)
        i+=1 
        if tmp >= n:
            break
    print(i)