
def solution(genres, plays):
    answer = []

    genresDict = dict()
    for i in range(len(genres)):
        if genres[i] not in genresDict.keys(): genresDict[genres[i]] = []
        genresDict[genres[i]].append(i)

    genresDict_sorted = {k: v for k, v in sorted(genresDict.items(), key = lambda x: sum(map(lambda q: plays[q], x[1])), reverse= True)}


    for (gernre, values) in genresDict_sorted.items():
        for number in sorted(values, key = lambda x: plays[x], reverse= True)[:2]:
            
            answer.append(number)


    return answer