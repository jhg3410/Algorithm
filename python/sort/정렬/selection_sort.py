def selection_sort(n):
    for i in range(n-1):
        min = i
        print(min)
        for j in range(i+1, n):
            if A[j] < A[min]:
                min = j 
        A[i],A[min] = A[min],A[i]
        
    return A

A = [40,10,50,90,20,80,30,60]
print(selection_sort(8))     