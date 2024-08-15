user_ids = []
banned_ids = []
finds = []


def solution(user_id, banned_id):
    global user_ids, banned_ids

    user_ids = user_id
    banned_ids = banned_id

    check_all_case([], 0)

    return len(finds)


def check_all_case(check: list, find: int):
    if len(check) == len(banned_ids):
        check = sorted(check)
        if check not in finds:
            finds.append(check)
            print(check)
        return

    for i in range(len(user_ids)):
        if i in check: continue
        if is_banned(user_ids[i], banned_ids[find]):
            new_check = check.copy()
            new_check.append(i)
            check_all_case(check=new_check, find=find + 1)


def is_banned(uid: str, bid: str):
    if len(uid) != len(bid): return False
    for idx, char in enumerate(uid):
        if bid[idx] == '*': continue
        if char != bid[idx]: return False

    return True