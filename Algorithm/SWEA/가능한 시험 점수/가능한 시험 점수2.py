# def top(d,s):
#     global m
#     d+=1
#     if B<=s<m:
#         m=s
#         return
#     if d== N:return
#     else:
#         top(d,s)
#         top(d,s+h[d])
# tc = int(input())
# for _ in range(tc):
#     N,B=list(map(int,input().split()))
#     h=list(map(int,input().split()))
#     m=sum(h)
#     top(-1,0)
#     print(f'#{_+1} {m-B}')

import sys
sys.stdin = open('sample_input.txt','r')
def check(depth, sum_):
    depth += 1
    if visited[sum_] == 0:
        visited[sum_] = depth
    if depth == N:
        return
    else:
        if visited[sum_ + scores[depth]] == 0:
            check(depth, sum_ + scores[depth])
        if visited[sum_] == 0:
            check(depth, sum_)

testcases = int(input())
for _ in range(testcases):
    N = int(input())
    scores = list(map(int,input().split()))
    visited = [0] * (sum(scores) + 1)
    check(-1,0)
    cnt = 0
    for _ in visited:
        if _ != 0:
            cnt += 1
    print(cnt)