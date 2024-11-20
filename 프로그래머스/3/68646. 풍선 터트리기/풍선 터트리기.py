def solution(a):
    answer = 0
    counts = [0 for _ in range(len(a))]
    
    left_min = a[0]
    for i in range(1, len(a)):
        if a[i] > left_min:
            counts[i] += 1
        else:
            left_min = a[i]
            
    right_min = a[-1]
    for i in range(len(a)-2, -1, -1):
        if a[i] > right_min:
            counts[i] += 1
        else:
            right_min = a[i]
    
    
    return len(list(filter(lambda x: x!=2, counts)))