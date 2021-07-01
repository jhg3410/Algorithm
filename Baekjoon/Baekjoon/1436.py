n = int(input())

six_n = 666
cnt = 0

while True:
    if '666'  in  str(six_n):
        cnt += 1
    
    if cnt == n:
        print(six_n)
        break

    six_n += 1