import sys
sys.stdin = open('input.txt','r')

def percent(depth, multi):
    global max_
    depth += 1
    if depth == N:
        if max_ < multi:
            max_ = multi
            return
    if multi == 0:
        return
    if multi < max_:
        return
    else:
        for _ in range(N):
            if visited[_] == False:
                visited[_] = True
                percent(depth, multi*mat[depth][_]*0.01)
                visited[_] = False

testcases = int(input())
for tc in range(testcases):
    N = int(input())
    mat = [list(map(float,input().split())) for _ in range(N)]
    visited = [False for _ in range(N)]
    max_ = -1
    percent(-1, 1)
    print('#{} {:.6f}'.format(tc+1,round(max_*100, 6)))

# from itertools import permutations
#
# def percent(depth, lis):
#     global max_, temp
#     depth += 1
#     if depth == N:
#         return
#     else:
#         temp *= mat[depth][lis[depth]]*0.01
#         percent(depth, lis)

# testcases = int(input())
# for tc in range(testcases):
#     N = int(input())
#     mat = [list(map(int,input().split())) for _ in range(N)]
#     li = [_ for _ in range(N)]
#     per_li = list(permutations(li))
#     max_ = -1
#     for _ in per_li:
#         temp = 1
#         percent(-1, _)
#         if max_ < temp * 100:
#             max_ = temp * 100
#     print(f'#{tc+1} {round(max_, 7)}')
