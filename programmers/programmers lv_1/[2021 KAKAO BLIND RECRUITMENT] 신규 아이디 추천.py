def solution(new_id):
    cnt = 0
    new_id = new_id.lower()
    lst = []
    for i in new_id:
        if i.islower() or  i.isdigit() or i == "-" or i =="_" or i==".":
            lst.append(i)
    for i in range(len(lst)-1):
        if lst[i] == '.' and lst[i+1] == '.':
            del lst[i]
            lst.insert(0,'')
            cnt += 1
    for q in range(cnt):
        lst.remove("")
    if len(lst) != 0:
        if lst[0] ==".":
            del lst[0]       

    if len(lst) != 0:
        if lst[-1] == ".":
            del lst[-1]
    if len(lst) == 0:
        lst.append('a')

    if len(lst) >= 16:
        lst = lst[:15]
    if lst[-1] == ".":
        del lst[-1]

    if len(lst) <= 2:
        while len(lst) !=3:
            lst.append(lst[-1])

    lst = ''.join(lst)

    return lst