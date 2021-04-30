def shell_sort(A,n):  # 간격(h)를 어떻게 할 것인지가 관건
    h_lst = []  # n마다 달라야함으로  각 경우에 맞도록 만들었다
    h = n // 2      # n//2로 처음 h를 넣고
    while True:
        h_lst.append(h)
        if h == 1:
            break
        h = h // 2     # h를 2로 나누면서 계속해서 넣어준다. if문을 중간에 넣어 1을 한번 참조하도록 하였다.
    for h in h_lst:   # h_lst에 있는 요소들을 하나씩 h에 넣으면서 반복문 실행
        for i in range(h,n):    # h부터 n-1까지 i에 대입
            currentelement = A[i]   # i의 값을 변수에 저장하고
            j = i   # i자체를 j에 넣어준다
            while j>=h and A[j-h]>currentelement:   # h(간격)을 j에 빼주면서 currentelement 와 비교
                A[j] = A[j-h]   # 만약 더 크다면 앞의 값을 j에 넣어주고
                j = j-h     # j를 h만큼 빼서 다시 반복문 실행
            A[j]= currentelement    # 반복문이 끝나면 currentelement 를 j인덱스에 넣어준다
    return A

