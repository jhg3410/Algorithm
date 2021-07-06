

while True:    
    n = list(map(int,input()))

    if  n[0] == 0:
        break

    real_n = list(reversed(n))
    if n == real_n:
        print("yes")
    else:
        print("no")
    
    