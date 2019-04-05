import sys
sys.stdin = open('sample_input.txt','r')

import collections

testcases = int(input())
for tc in range(testcases):
    N = int(input()) # 시험 문제 갯수
    scs = list(map(int,input().split())) # 점수 배점
    vi = [True] * len(scs) # 시험 문제 체크
    vi2 = [True] * (sum(scs) + 1) # 배점 체크
    dq = collections.deque()
    dq.append([0, vi])
    cnt = 1
    while dq:
        w, vi = dq.popleft()
        for _ in range(len(scs)):
            if w + scs[_] <= sum(scs) and vi2[w+scs[_]] and vi[_]:
                vi2[w+scs[_]] = False # 배점 중복 체크
                temp = vi[:]
                temp[_] = False # 시험 문제 중복 체크
                dq.append([w + scs[_],temp])
                cnt += 1
    print(f'#{tc + 1} {cnt}')