n = int(input())
star = 2 * n - 1


for i in range(n-1):
    print(" "* i  + (star - (i*2)) * '*')

for i in range(n-1, -1 , -1):
    print(" "* i  + (star - (i*2)) * '*')