def div(s, g):
    mid = (s + g) // 2
    temp_ti = 0
    for _ in ti:
        temp_ti += mid // _
    if s == g:
        print(mid)
        return
    else:
        if temp_ti < M:
            div(mid + 1, g)
        elif M <= temp_ti:
            div(s, mid)

N, M = list(map(int,input().split()))
ti = []

for _ in range(N):
    ti.append(int(input()))

min_max = min(ti) * M

div(0, min_max)