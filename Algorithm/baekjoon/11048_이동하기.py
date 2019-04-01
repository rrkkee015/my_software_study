# import collections
#
# # input을 받읍시다.
# N, M = list(map(int,input().split()))
# mat = [list(map(int,input().split())) for _ in range(N)]
#
# # 사용 할 친구들을 만듭시다.
# max_ = 0
# dq = collections.deque()
# dxdy = [(1,0),(0,1),(1,1)]
#
# # 초기값을 dq에 넣읍시다.
# dq.append([0,0,mat[0][0]]) # y, x, 사탕의 cnt
#
# # BFS를 돌립시다.
# while dq:
#     y, x, cnt = dq.popleft()
#     for _ in dxdy:
#         if 0 <= y + _[0] < N and 0 <= x + _[1] < M:
#             dq.append([y + _[0], x + _[1], cnt + mat[y + _[0]][x + _[1]]])
#     # 그 중 최댓값을 가져옵시다.
#     if max_ < cnt:
#         max_ = cnt
# print(max_)

# 이 문제는 BFS로 푸는 문제가 아니다. 최단 경로를 구하는 것도 아니고 최댓값을 구하는 문제다보니 BFS로 풀다간 메모리초과를 맞는다.

# input을 받습니다.
N, M = list(map(int,input().split()))
mat = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
dp[0][0] = mat[0][0]
# 필요한 친구를 만듭니다.
max_ = 0

# matrix를 순회합니다.
for i in range(N):
    for j in range(M):
        if 0 <= i-1 < N and 0 <= j-1 < M:
            dp[i][j] = max(dp[i-1][j] + mat[i][j], dp[i][j-1] + mat[i][j], dp[i-1][j-1] + mat[i][j], dp[i][j])
        elif 0 <= j-1 < M:
            dp[i][j] = max(dp[i][j-1] + mat[i][j], dp[i][j])
        elif 0<= i-1 < N:
            dp[i][j] = max(dp[i-1][j] + mat[i][j], dp[i][j])
print(dp[-1][-1])