# from itertools import permutations
# N = int(input())
# t = list(map(int,input().split()))
# t = list(permutations(t))
# min = 10 ** 9
# for _ in t:
#     temp = _[0]
#     li = _[0]
#     for i in range(len(_)-1):
#         temp += _[i+1]
#         li += temp
#     if min > li:
#         min = li
# print(min)

# def permu(n, k):
#     if k == n:
#         if li not in t:
#             t.append(li[:])
#     else:
#         for i in range(k, n):
#             li[i], li[k] = li[k], li[i]
#             permu(n, k+1)
#             li[i], li[k] = li[k], li[i]
#
# N = int(input())
# li = list(map(int,input().split()))
# t = []
# permu(N,0)
# min = 10 ** 9
# for _ in t:
#     temp = _[0]
#     li = _[0]
#     for i in range(len(_)-1):
#         temp += _[i+1]
#         li += temp
#     if min > li:
#         min = li
# print(min)

# 순열 아님

N = int(input())
t = sorted(list(map(int,input().split())))
result = 0
i = 0
for _ in range(len(t)):
    result += t[_] * (N - _)
print(result)