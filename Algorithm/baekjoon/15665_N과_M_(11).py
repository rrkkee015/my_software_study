# import itertools
# N,M = map(int,input().split())
# lis = sorted(list(map(int,input().split())))
# result = []
# for _ in itertools.product(lis, repeat=M):
#     result.append(_)
# for _ in sorted(list(set(result))):
#     print(*_)

# N, M = map(int, input().split())
# arr = sorted(set(map(int, input().split())))
#
# def dfs(selected, i):
#     if i == M:
#         print(' '.join(list(map(str, selected))))
#     else:
#         for n in arr:
#             dfs(selected+[n], i+1)
#
# dfs([], 0)

import itertools
N,M = map(int,input().split())
li = list(set(map(int,input().split())))
for _ in itertools.product(sorted(li), repeat= M):
    print(*_)