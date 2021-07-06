n = int(input())

for _ in range(n):
    x_1,y_1,r_1,x_2,y_2,r_2 = map(int,input().split())
    
    d = ((x_1-x_2)**2 + (y_1-y_2)**2)**0.5
    
    r_sum = r_1 + r_2
    r_diff = abs(r_1 - r_2)

    if d == 0:
        if r_diff == 0:
            print(-1)
        else:
            print(0)
    elif d < r_sum and d > r_diff:
        print(2)

    else:
        if r_sum == d:
            print(1)
        elif r_diff == d:
            print(1)
        else:
            print(0)
    
