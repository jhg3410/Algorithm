n = int(input())
customers = list(map(int, input().split()))
leader, member = map(int, input().split())
answer = 0

for customer in customers:
    remain = customer
    remain -= leader
    answer += 1

    if remain <= 0: continue
    if remain % member == 0:
        answer += remain // member
    else:
        answer += (remain // member) + 1

print(answer)