## 작업 스케줄링

### 작업,작업의 수행시간, 기계가 주어질 때 모든 작업이 가장 빨리 종료되도록 기계에 작업을 배정하는 알고리즘입니다.  
### 근사 알고리즘  
```python

def solve(n,m,t):
    L = []      # 리스트 생성
    for j in range(m):
        L.append(0)     # 리스트에 0으로 초기화
    for i in range(n):
        min = 0     # 비교값 지정
        for j in range(m):
            if L[j] < L[min]:    # m(기계 수)인덱스의 L값과 비교값과 비교후 L[j]가 더 작으면
                min = j     # min값 새로고침
        L[min] += t[i]      # L에 가장 작은 값에 t의 각 요소를 추가
    return max(L)        # for문이 다 돈 후 마무리된 L의 최대값 반환

```

main(입출력)은 교체하면서 진행 할 예정이라 해결 함수만 보겠습니다.  
먼저 기계에 작업(수행시간)을 배정할 리스트를 생성하고 기계의 수 만큼 리스트를 0으로 초기화 시켜줍니다.  
그러고는 작업의 수만큼 min(비교,최솟값)을 0으로 초기화하고 다시 m만틈 돌면서
각 리스트의 요소를 하나씩 비교하면서 가장작은 index를 찾아 min값을 새로고침해준다.  
그러면 L[min]은 리스트에서 가장 최솟값이 된다. 거기에 t의 각 요소를 추가해주면서 작업을 n(작업의 수)만큼 for 문을 돌려주면 마무리된 L이 나온다.  
마지막으로 L에서 가장 높은값(작업시간이 가장 긴 기계)를 반환 시켜준다.  

이 알고리즘에서 구하는 값은 근사값이다. 코드안에 보다시피 t의 인덱스 순서로 추가하기때문에 정렬을 하지않고 순서대로 넣다보니 최적해가아닌 근사해가 나온다.  
- - -
### 최적 알고리즘  
``` python 
def solve_optimal(n,m,t):
    t.sort(reverse=True)    # 시간리스트를 내림차순으로 정렬
    L = []      # 리스트 생성
    for j in range(m):
        L.append(0)     # 리스트에 0으로 초기화
    for i in range(n):
        min = 0     # 비교값 지정
        for j in range(m):
            if L[j] < L[min]:    # m(기계 수)인덱스의 L값과 비교값과 비교후 L[j]가 더 작으면
                min = j     # min값 새로고침
        L[min] += t[i]      # L에 가장 작은 값에 t의 각 요소를 추가
    return max(L)     # for문이 다 돈 후 마무리된 L의 최대값 반환
```
위 알고리즘은 제가 최적해를 구하는 알고리즘이라 생각하고 구현한 알고리즘입니다.  
어떻게 짜야할지 고민을 많이 했는데 근사해를 구하는 코드가 왜 근사해인지 생각해서 t를 내림차순으로 정렬한다면 내림차순 순서로  
이제 리스트의 최솟값 인덱스에 추가되면서 최적의 값이 초래될 수 있다 생각했다.  
- - -
### 결과값
``` python
import random   # 난수를 사용하기 위해 random 모듈 import
import timeit   # 시간측정을 위해 import
from Job_Scheduling import solve    # 함수 사용을 위해 import
from Job_Scheduling_optimal import solve_optimal    # 함수 사용을 위해 import

n = [4,8,16]   # 작업 수
m = 2     # 기계 수
for i in range(len(n)):
    t = []
    for j in range(n[i]):
        t.append(random.randrange(1,10))    # 각 작업의 소요시간
        
    start = timeit.default_timer()      # 시작 시간
    print("작업수 :",n[i],"의","근사해 :",solve(n[i],m,t))  #
    print("근사 알고리즘의 실행시간 :",timeit.default_timer()-start,"초 걸렸습니다")    # 현재시간 - 시작시간 = 실행시간
    start = timeit.default_timer()
    print("작업수 :",n[i],"의","최적해 :",solve_optimal(n[i],m,t))
    print("최적 알고리즘의 실행시간 :",timeit.default_timer()-start,"초 걸렸습니다")
    
```
위의 함수에 위 코드로 실행하면  
![image](https://user-images.githubusercontent.com/80373033/118423603-5b06fe00-b700-11eb-8460-556f3420180e.png)  
위 처럼 결과가 나온다. 최적해가 근사해보다 더 적게 나오지만 실행시간은 최적해 코드가 더 오래 걸리는 것을 알 수 있다.
