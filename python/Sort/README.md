# sort  
### 선택정렬과 삽입정렬, 쉘정렬들을 먼저 구현하고 설명한 다음 각 배열의 정렬된 정도에 따른 시간복잡도를 알아보겠습니다.  
- - - 
## 선택정렬  
``` python 
def selection_sort(A,n):
    for i in range(n-1): # 0 부터 n-2까지 i를 참조한다 그래야 밑의 반복문에서 배열의 범위를 안 넘어간다
        min = i # 최솟값
        for j in range(i+1, n):  
            if A[j] < A[min]:  # 최솟값과 최솟값 다음의 index들을 비교해서 최솟값이 더 크다면
                min = j     # 최솟값 교체
        A[i],A[min] = A[min],A[i]   # 그리고는 i와 최솟값의 위치를 바꿔준다.
        # 2중반복문으로 모든 원소들을 모두 비교하면서 정렬한다.
    return A
```
### 설명  
반복문을 돌면서 최솟값에 0부터 n-2까지 넣어주고 2중 반복문으로 최솟값과 다음 index의 값들을 비교해서  
가장 작은 값을 최솟값으로 새로고침해준다. 반복문이 최솟값을 찾으면 기존의 i와 위치를 교체시켜준다.  
- - -
##  삽입정렬  
``` python
def insertion_sort(A,n):
    for i in range(1,n):    # 1부터 n-1까지
        currentelement = A[i]   # 인덱스의 값
        j  = i - 1  
        while j>=0 and A[j] > currentelement:   # i 인덱스의 값과 j의 인덱스 값을 비교 j가 더 크다면
            A[j+1] = A[j]   # j의 값을 새로고침
            j = j -1    # 앞의 값을 비교하기 위해 -1 해준다.
        A[j+1] = currentelement # 반복문이 끝나면 i의 값(currentelement)을 j+1에 넣어준다.

    return A
```
### 설명  
삽입 정렬은 하나씩 찾아가는 느낌이다. 반복문을 돌면서 먼저 현재의 값을 변수의 저장하고 j변수(i-1)를 또 하나 만들고  
만약 j값이 현재의 값보다 크다면 j를 뒤로 땅겨주고 j를 하나씩 빼주면서 반복문을 돈다. 그러면 while문이 빠져 나올때 까지  
j를 계속 뒤로 하나씩 밀려주고 빠져나오면 current값을 j+1에 넣어준다.  
- - -  
## 쉘 정렬  
``` python
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
```
### 설명  
쉘 정렬은 삽입정렬하고 매우 비슷하다. 다른건 간격을 크게 한 것이다. 삽입정렬은 간격을 1로 하나씩 비교했지만  
쉘 정렬은 간격을 지정해서 비교해준다. 제가 짠 코드에선 h_lst라는 간격을 넣을 배열을 만들어주고 n에 2씩 나눠주면서 h_lst에 넣어주었다.  
h가 1한번을 허용하고 또 1이 나오면 while문을 빠져나오게 하였다.  
그리곤 h_lst 에 요소들을 하나씩 꺼내서 2중반복문을 돌린다. 다음 코드부터는 삽입정렬하고 거의 유사하다.  
현재 값을 넣어주는데 h부터 넣어준다. 그러고는 j변수를 i와 같게 만들어주고 간격만큼 j를 뺴주면서 현재값과 비교하면서  
삽입정렬처럼 반복문이 나올때 까지 옮겨주고 나오면 currentelement값을 j인덱스에 넣어준다.  
- - -
## Main
``` python
import insertion_sort
import selection_sort
import shell_sort
import timeit

A = [10,20,30,40,90,80,70,60,50]    # 어느정도 정렬이 되어있는 배열
A = [90,80,70,60,50,40,30,20,10]    # 정렬이 전혀 되어있지않은 배열
n = len(A)
start_time = timeit.default_timer()
print("정렬된 배열 :",selection_sort.selection_sort(A,n))
print("선택정렬의 시간은 : ",timeit.default_timer()-start_time)
start_time = timeit.default_timer()
print("정렬된 배열 :",insertion_sort.insertion_sort(A,n))
print("삽입정렬의 시간은 : ",timeit.default_timer()-start_time)
start_time = timeit.default_timer()
print("정렬된 배열 :",shell_sort.shell_sort(A,n))
print("쉘 정렬의  시간은 : ",timeit.default_timer()-start_time)
```
미리 정의한 정렬들을 import 받아서 실행시켰다.
두개의 배열을 초기화 한 이유는 시간복잡도를 비교해보기 위해서이다.  
출력값을 위의 A먼저 보여드리고 비교한 다음 2번쨰 A로 실행해서 비교하겠습니다.  
### 어느정도 정렬이 되어있는 배열  
* 출력  
![image](https://user-images.githubusercontent.com/80373033/116665175-60f8a180-a9d4-11eb-8599-a766cb7af788.png)  
보시면 어느정도 정렬이 되어있으면   
걸린 시간은 선택정렬 > 삽입정렬 > 쉘 정렬 이다.  
성능은 반대로 쉘정렬 > 삽입정렬 > 선택정렬 이다.  
###  정열이 전혀 되어있지않은 배열  
* 출력  
![image](https://user-images.githubusercontent.com/80373033/116665103-4c1c0e00-a9d4-11eb-88d9-c0900ed012f8.png)  
보시면 정렬이 되어있지 않으면  
걸린 시간은 선택정렬 > 삽입정렬 > 쉘 정렬 이다.  
성능은 반대로 쉘정렬 > 삽입정렬 > 선택정렬 이다.
하지만 많이 실행 하다보면 쉘정렬은 항상 성능이 가장 좋지만  
삽입과 선택은 엎치락 뒤치락한다.  
결국 쉘정렬 > 삽입정렬 = 선택정렬 볼 수 있다.  
여기서 알 수 있는 것은 쉘 정렬이 가장 좋고 어느 정도 정렬이 되어있으면 삽입 > 선택  
정렬이 되어있지 않으면 삽입 == 선택이다.  

## 그래프 표현
