N, K = list(map(int,input().split()))
top = 1
bottom = 1
for _ in range(0,K):
    top*=N
    N-=1
for _ in range(1, K+1):
    bottom*=_
print(int(top//bottom)%10007)