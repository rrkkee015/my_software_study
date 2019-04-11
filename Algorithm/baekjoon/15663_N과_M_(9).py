# def permu(li):
#     if len(li) == M:
#         if li not in result:
#             result.append(li)
#     else:
#         for _ in range(len(lis)):
#             if visited[_]:
#                 visited[_] = 0
#                 permu(li + [lis[_]])
#                 visited[_] = 1
#
# N, M = map(int,input().split())
# lis = sorted(list(map(int,input().split())))
# visited = [1 for _ in range(N)]
# result = []
# permu([])
# for _ in result:
#     print(*_)

# 시간 초과

# import itertools
# N, M = map(int,input().split())
# lis = sorted(list(map(int,input().split())))
# result = []
# for _ in itertools.permutations(lis, M):
#     if _ not in result:
#         result.append(_)
#         print(*_)

# 시간 초과

import itertools
N, M = map(int,input().split())
lis = sorted(list(map(int,input().split())))
result = []
for _ in itertools.permutations(lis, M):
    result.append(_)
for _ in sorted(list(set(result))):
    print(*_)