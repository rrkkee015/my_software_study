# def product(lis):
#     if len(lis) == M:
#         print(' '.join(lis))
#     else:
#         for _ in li:
#             lis.append(str(_))
#             product(lis)
#             lis.pop()
# N, M = list(map(int,input().split()))
# li = [_+1 for _ in range(N)]
# product([])
#
# import itertools
#
# N, M = list(map(int,input().split()))
# li = [str(_ + 1) for _ in range(N)]
# for _ in itertools.product(li, repeat=M):
#     print(' '.join(_))

def permu_pro(lis):
    if len(lis) == M:
        print(lis)
    else:
        for _ in arr:
            permu_pro(lis + [_])
N,M = map(int,input().split())
arr = [_ + 1 for _ in range(N)]
permu_pro([])