def solution(seoul):
    for index , value in enumerate(seoul):
        if value == "Kim":
            return "김서방은 "+str(index)+"에 있다"
    