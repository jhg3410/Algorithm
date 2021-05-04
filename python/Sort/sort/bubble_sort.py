def bubble_sort(A,n):
    for i in range(1,n):
        for j in range(1,n-i+1):
            if(A[j-1] > A[j]):
                A[j-1] ,A[j] = A[j], A[j-1]

    return A
