# def product(li):
#     if len(li) == M:
#         print(*li)
#     else:
#         for _ in lis:
#             li.append(_)
#             product(li)
#             li.pop()
#
# N, M = map(int,input().split())
# lis = sorted(list(map(int,input().split())))
# product([])

# import itertools
# N, M = map(int,input().split())
# lis = sorted(list(map(int,input().split())))
# for _ in itertools.product(lis, repeat = M):
#     print(*_)

def dfs(depth, li):
    depth += 1
    if depth == M:
        print(*li)
    else:
        for _ in range(len(lis)):
            dfs(depth, li + [lis[_]])

N, M = map(int,input().split())
lis = sorted(list(map(int,input().split())))
dfs(-1, [])