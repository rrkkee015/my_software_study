def collections(n, r):
    global cnt
    if r == 0:
        cnt += 1
    elif r > n:
        return
    else:
        K_li[r-1] = N_li[n-1]
        collections(n-1,r-1)
        collections(n-1,r)

N, K = list(map(int,input().split()))
N_li = [_ for _ in range(N)]
K_li = [0 for _ in range(K)]
cnt = 0
collections(N, K)
print(cnt)