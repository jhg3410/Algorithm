x , y = map(int,input().split())

if x < y :
    x, y = y, x

print(x + y + (y // 10))