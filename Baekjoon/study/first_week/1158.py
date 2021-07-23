n, k = map(int,input().split())
lst = [i for i in range(1,n+1)]
answer = []

num = 0

while len(lst) >0:
    num += (k - 1)
    if num +1 > len(lst):
        num = num % len(lst)
    answer.append(str(lst.pop(num)))

print("<"+", ".join(answer)+">")

