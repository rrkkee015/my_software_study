import sys
sys.stdin = open('input.txt','r')

testcases = int(input())
for tc in range(testcases):
    print('#{}'.format(tc + 1))
    N = int(input())
    mat = [[0] * N for _ in range(N)]
    ewsn = [(0,1),(1,0),(0,-1),(-1,0)]
    num = 1
    index = 0
    y,x = 0,0
    dy,dx = ewsn[index]
    while num != N*N+1:
        mat[y][x] = str(num)
        num += 1
        y += dy
        x += dx
        if 0 <= y + dy < N and 0 <= x + dx < N and mat[y + dy][x + dx] == 0:
            continue
        else:
            index += 1
            if index > 3:
                index = 0
            dy,dx = ewsn[index]
    for i in mat:
        print(' '.join(i))