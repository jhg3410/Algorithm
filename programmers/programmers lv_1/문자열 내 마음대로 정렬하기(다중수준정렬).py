def solution(strings, n):
    temp = []
    answer = []
    for word in strings:
        word = word[n] + word
        temp.append(word)

    temp.sort()

    for i in temp:
        answer.append(i[1:])

    return answer

from operator import itemgetter

def solution(strings, n):
    return sorted(sorted(strings), key=itemgetter(n))