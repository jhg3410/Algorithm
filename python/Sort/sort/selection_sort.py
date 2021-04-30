def selection_sort(A,n):
    for i in range(n-1): # 0 부터 n-2까지 i를 참조한다 그래야 밑의 반복문에서 배열의 범위를 안 넘어간다
        min = i # 최솟값
        for j in range(i+1, n):  
            if A[j] < A[min]:  # 최솟값과 최솟값 다음의 index들을 비교해서 최솟값이 더 크다면
                min = j     # 최솟값 교체
        A[i],A[min] = A[min],A[i]   # 그리고는 i와 최솟값의 위치를 바꿔준다.
        # 2중반복문으로 모든 원소들을 모두 비교하면서 정렬한다.
    return A
