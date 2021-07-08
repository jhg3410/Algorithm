def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)

n = int(input())

answer = factorial(n)
answer = list(reversed(str(answer)))
for a in answer:
    if a != '0':
        print(answer.index(a))
        break