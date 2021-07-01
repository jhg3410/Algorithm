def solution(n, m):
    GCD = gcd(n,m)
    LCM = (n*m) // GCD
    answer = []
    answer.append(GCD)
    answer.append(LCM)
    
    return answer

def gcd(n,m):
    if n>m:
        (n,m) = (m,n)
    if m % n == 0:
        return n
    else:
        return gcd(n,m%n)