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
    