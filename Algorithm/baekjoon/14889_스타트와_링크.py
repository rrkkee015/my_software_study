from itertools import combinations

# def combi(n, r):
#     if r == 0:
#         re.append(com[:])
#     elif n < r:
#         pass
#     else:
#         com[r-1] = li[n-1]
#         combi(n-1, r-1)
#         combi(n-1, r)
#
# def combist(n, r, lis):
#     global st
#     if r == 0:
#         i = comst[0] - 1
#         j = comst[1] - 1
#         st += mat[i][j] + mat[j][i]
#     elif n < r:
#         pass
#     else:
#         comst[r-1] = lis[n-1]
#         combist(n-1, r-1, lis)
#         combist(n-1, r, lis)
#
# def combilin(n, r):
#     global lin
#     if r == 0:
#         i = comlin[0] - 1
#         j = comlin[1] - 1
#         lin += mat[i][j] + mat[j][i]
#     elif n < r:
#         pass
#     else:
#         comlin[r-1] = temp[n-1]
#         combilin(n-1, r-1)
#         combilin(n-1, r)
#
# N = int(input())
# li = [_ for _ in range(N)]
# com = [0 for _ in range(N//2)]
# re = []
# mat = [list(map(int,input().split())) for _ in range(N)]
# min = 10**9
# combi(N, N//2)
# comst = [0, 0]
# comlin = [0, 0]
# for _ in range(len(re)):
#     st = 0
#     lin = 0
#     temp = []
#     print(re[_])
#     for __ in li:
#         if __ not in re[_]:
#             temp.append(__)
#     combist(len(re[_]), 2, re[_])
#     combilin(len(re[_]), 2)
#     if min > abs(st - lin):
#         min = abs(st - lin)
# print(min)

# N = int(input())
# lis = [_ for _ in range(N)] # 위치 리스트
# mat = [list(map(int,input().split())) for _ in range(N)] # 시너지 보드
# st = list(combinations(lis,N//2)) # st 조합 가능성
# lin = [] # lin 조합 가능성
# min_ = 10**9 # 최솟값
# for _ in st: # st 팀을 기반으로 lin 팀 만들기
#     temp = []
#     for __ in lis:
#         if __ not in _:
#             temp.append(__)
#     lin.append(temp)
# for _ in range(len(st)): # st 팀 갯수만큼 돌면서
#     st_sc = list(combinations(st[_], 2)) # 2명씩 뽑아서 점수를 측정하자
#     lin_sc = list(combinations(lin[_],2)) # 얘도 마찬가지
#     s_sc = 0
#     l_sc =0
#     for __ in st_sc: # 2명씩 뽑은 경우 순회하면서
#         i = __[0]
#         j = __[1]
#         s_sc += mat[i][j] + mat[j][i] # 점수에 더하자
#     for __ in lin_sc:
#         i = __[0]
#         j = __[1]
#         l_sc += mat[i][j] + mat[j][i]
#     if min_ > abs(s_sc - l_sc): # 최솟값 비교
#         min_ = abs(s_sc - l_sc)
# print(min_) # 끝

# 굳이 하나의 리스트에서 또 2개로 나눌 필요 없이 앞에서 오면 st 팀이고 뒤에서 오면 lin 팀이라서 그렇게 순회하면 더 편하다.
# 그리고 팀 가능성에서 2명씩 뽑아서 점수를 매겼는데 그것도 그냥 for 문 2번으로 해결 가능하다. 0 잡고 나머지 순회하고 1 잡고 나머지 순회 하는거랑 같다.

N = int(input())
mat = [list(map(int,input().split())) for _ in range(N)]
lis = [_ for _ in range(N)]
div = list(combinations(lis, N//2))
min_ = 10**9
for _ in range(len(div)//2):
    st = div[_]
    li = div[len(div)-1-_]
    st_ = list(combinations(st, 2))
    li_ = list(combinations(li, 2))
    s_st = 0
    s_li = 0
    for __ in st_:
        i = __[0]
        j = __[1]
        s_st += mat[i][j] + mat[j][i]
    for __ in li_:
        i = __[0]
        j = __[1]
        s_li += mat[i][j] + mat[j][i]
    if min_ > abs(s_st - s_li):
        min_ = abs(s_st - s_li)
print(min_)