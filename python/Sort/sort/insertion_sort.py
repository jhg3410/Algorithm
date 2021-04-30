def insertion_sort(A,n):
    for i in range(1,n):    # 1부터 n-1까지
        currentelement = A[i]   # 인덱스의 값
        j  = i - 1  
        while j>=0 and A[j] > currentelement:   # i 인덱스의 값과 j의 인덱스 값을 비교 j가 더 크다면
            A[j+1] = A[j]   # j의 값을 새로고침
            j = j -1    # 앞의 값을 비교하기 위해 -1 해준다.
        A[j+1] = currentelement # 반복문이 끝나면 i의 값(currentelement)을 j+1에 넣어준다.

    return A
