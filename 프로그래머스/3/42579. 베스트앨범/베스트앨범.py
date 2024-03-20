from collections import defaultdict

def solution(genres, plays):
    answer = []
    genresDict = defaultdict(list)

    for i in range(len(genres)):
        genresDict[genres[i]].append(i)

    genresDict_sorted = sorted(genresDict.values(), key = lambda x: sum(map(lambda q: plays[q], x)), reverse= True)

    for values in genresDict_sorted:
        answer.extend(sorted(values, key = lambda x: plays[x], reverse= True)[:2])

    return answer