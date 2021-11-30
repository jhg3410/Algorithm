import math
def solution(n, words):
    answer = []

    tmp = []
    for word in words:
        if len(word) == 1:
            break
        if not tmp:
            tmp.append(word)
        else:
            if word in tmp:
                break
            if word[0] != tmp[-1][-1]:
                break
            tmp.append(word)

    cnt  = len(tmp)+1
    if cnt > len(words):
        return [0,0]
    else:
        if cnt % n  == 0:  answer.append(n)
        else:  answer.append(cnt % n)

        answer.append(math.ceil(cnt/n))

        return answer

n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n,words))