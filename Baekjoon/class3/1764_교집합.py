n, m = map(int,input().split())
listen = set(input().strip() for _ in range(n))
see = set(input().strip() for _ in range(m))

answer = sorted(list(listen & see))

print(len(answer))
print('\n'.join(a for a in answer))