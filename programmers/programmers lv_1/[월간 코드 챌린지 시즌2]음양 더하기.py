def solution(absolutes, signs):
    sum = 0
    for i in range(len(absolutes)):
        if signs[i] == 'true':
            sum += absolutes[i]
        else:
            sum -= absolutes[i]
    
    return sum

abs = [4,7,12]
signs=["true","false","true"]

print(solution(abs,signs))