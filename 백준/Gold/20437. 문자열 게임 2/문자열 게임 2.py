def game(word, k):
    alphabets = [[] for _ in range(26)]
    maxAnswer = -1
    minAnswer = 10 ** 5
    for i in range(len(word)):
        alphabets[ord(word[i])-97].append(i)
    
    for idx in alphabets:
        for i in range(0, len(idx) - k + 1):
            maxAnswer= max(maxAnswer, idx[i+k-1] - idx[i] + 1)
            minAnswer= min(minAnswer, idx[i+k-1] - idx[i] + 1)

    return [maxAnswer, minAnswer]


results = []
for _ in range(int(input())):
    word, k = [input() for _ in range(2)]
    maxResult, minResult = game(word, int(k))
    results.append([maxResult, minResult])
   
for result in results:   
    maxResult, minResult = result[0], result[1]
    if maxResult == -1:
        print(-1)
    else:
        print(str(minResult)+" "+str(maxResult))
