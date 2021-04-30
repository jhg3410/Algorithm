def shell_sort(n):
    for h in [5,3,1]:
        for i in range(h,n):
            currentelement = A[i]
            j = i
            while j>=h and A[j-h]>currentelement:
                A[j] = A[j-h]
                j = j-h
            A[j]= currentelement
    return A

A = [40,10,50,90,20,80,30,60]
print(shell_sort(8))     