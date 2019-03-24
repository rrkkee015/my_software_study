# # def _(n):
# #     if n == 1 or n == 0:
# #         return 1
# #     else:
# #         return _(n-1)+_(n-2)
# #
# # print(_(100))
#
# def __(n):
#     for _ in range(n-1):
#         lis.append(lis[-1]+lis[-2])
#
# lis=[1,1]
# __(11)
# print(lis)
#
# def ___(n):
#     if n ==1 or n == 0:
#         return 1
#     if len(memo) > n:
#         return memo[n]
#     memo.append(___(n-1) + ___(n-2))
#     return memo[n]
#
# memo=[0,1,1]
# ___(5)
# print(memo)

def permu(n):
