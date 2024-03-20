
def solution(genres, plays):
    answer = []
    genresDict = dict()

    for i in range(len(genres)):
        if genres[i] not in genresDict.keys(): genresDict[genres[i]] = []
        genresDict[genres[i]].append(i)

    genresDict_sorted = sorted(genresDict.values(), key = lambda x: sum(map(lambda q: plays[q], x)), reverse= True)

    for values in genresDict_sorted:
        answer.extend(sorted(values, key = lambda x: plays[x], reverse= True)[:2])

    return answer
