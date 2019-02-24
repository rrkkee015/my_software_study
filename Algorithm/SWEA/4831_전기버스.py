def bus(x):
    global cnt
    now = x
    x += K
    if x >= N:
        print(f'#{tc+1} {cnt}')
        return 0
    elif x in M:
        cnt += 1
        bus(x)
        return 0
    else:
        for back in range(K):
            x -= 1
            if x in M and x != now:
                cnt += 1
                bus(x)
                return 0
            elif x == now:
                print(f'#{tc+1} 0')
                return 0


testcases=int(input())
for tc in range(testcases):
    K,N,M=tuple(map(int,input().split()))
    M=list(map(int,input().split()))
    cnt=0
    bus(0)
