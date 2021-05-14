import random 

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

n = 2**8   # 작업 수
m = 16     # 기계 수
t = []
for i in range(n):
    t.append(random.randrange(1,30))    # 각 작업의 소요시간

print(solve(n,m,t))