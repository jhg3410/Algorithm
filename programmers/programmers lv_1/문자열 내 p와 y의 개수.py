def solution(s):
    cnt_p = 0
    cnt_y = 0
    s = s.lower()
    for i in s:
        if i  == 'p':   cnt_p += 1
        elif i == 'y':   cnt_y += 1    

    if cnt_y == cnt_p: return True
    else: return False