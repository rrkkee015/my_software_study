# import itertools
# N, M = list(map(int,input().split()))
# lis = [_+1 for _ in range(N)]
# for _ in itertools.combinations_with_replacement(lis, M):
#     print(*_)
# def pro_combi(li):
#     if len(li) == M:
#         print(li)
#     else:
#         if li == []:
#             for _ in lis:
#                 pro_combi(li + [_])
#         else:
#             for _ in lis:
#                 if li[-1] <= _:
#                     pro_combi(li + [_])
# N, M = list(map(int,input().split()))
# lis = [_+1 for _ in range(N)]
# pro_combi([])

def combi(lis):
    if len(lis) == M:
        print(lis)
    else:
        for _ in arr:
            if lis == []:
                combi(lis + [_])
            else:
                if lis[-1] <= _:
                    combi(lis + [_])


N, M = map(int, input().split())
arr = [_ + 1 for _ in range(N)]
combi([])