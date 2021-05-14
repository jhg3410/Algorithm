import random 
import time
from Job_Scheduling import solve
from Job_Scheduling_optimal import solve_optimal

n = 2**16   # 작업 수
m = 16     # 기계 수
t = []
for i in range(n):
    t.append(random.randrange(1,30))    # 각 작업의 소요시간
start = time.time()
print("근사해 :",solve(n,m,t))
print("근사 알고리즘의 실행시간 :",time.time()-start)
start = time.time()
print("최적해 :",solve_optimal(n,m,t))
print("최적 알고리즘의 실행시간 :",time.time()-start)