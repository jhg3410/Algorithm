def solution(s):
    length = len(s)
    back_length = length//2
    front= s[:length-back_length]
    back= s[length-back_length:]
    back = back[::-1]
    i = 0
    answer= ''
    while True:
        if i < len(front):
            answer+=front[i]
        if i < len(back):
            answer+=back[i]
        if i >= len(front):
            break
        i += 1
    return answer


n= int(input())
s= input()
q = s
repeat = 0
while True:
    repeat += 1
    s = solution(s)
    if q==s:
        break

cnt = repeat - (n % repeat)

for _ in range(cnt):
    q = solution(q)    

print(q)