# from collections import deque
# N, K = list(map(int,input().split()))
# coins = deque()
# cnt = 0
# for _ in range(N):
#     coins.appendleft(int(input()))
# for _ in range(len(coins)):
#     if K >= coins[_]:
#         while K >= coins[_]:
#             K -= coins[_]
#             cnt += 1
# print(cnt)
# 덱을 이용

N, K = list(map(int,input().split()))
coins = []
cnt = 0
for _ in range(N):
    coins.append(int(input()))
coins = sorted(coins, reverse=True)
for _ in list(coins):
    if K >= _:
        tem = K//_
        K = K - tem*_
        cnt += tem
        # while K >= _:
        #     K -= _
        #     cnt += 1
        # while로 쓰면 시간초과 떠버린다.
print(cnt)
# 그냥 리스트 이용