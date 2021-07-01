# 에라토스테네스의 체 (소수 분별 빠르게)
def solution(n):
    sieve = [True] * (n+1)

    m = int(n**0.5)
    for i in range(2,m+1):
        if sieve[i] == True:
            for j in range(i+i, n+1 ,i):
                sieve[j] = False
    return  len([i for i in range(2,n+1) if sieve[i]== True])
    
print(solution(5))

# 에라토스테네스의 체 (소수 분별 빠르게)를 더욱 쉽게 속도는 위가 더빠름
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,int(n**0.5)+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

