N = int(input())
cnt=0
for _ in range(N-1, -1, -1):
    print(' ' * cnt + '*' * (2*(N-1)-(2*cnt-1)))
    cnt += 1