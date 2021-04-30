def insertion_sort(n):
    for i in range(1,n):
        currentelement = A[i]
        j  = i - 1
        while j>=0 and A[j] > currentelement:
            A[j+1] = A[j]
            j = j -1
        A[j+1] = currentelement

    return A
        
A = [40,10,50,90,20,80,30,60]
print(insertion_sort(8))