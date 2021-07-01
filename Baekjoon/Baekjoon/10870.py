n = int(input())

def fibonach(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonach(n-1) + fibonach(n-2))

print(fibonach(n))