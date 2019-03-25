# def permu(lis):
#     if len(lis) == M:
#         print(' '.join(lis))
#         return
#     else:
#         for _ in range(1,N+1):
#             if str(_) not in lis:
#                 lis.append(str(_))
#                 permu(lis)
#                 lis.pop()

def permu(depth):
    depth += 1
    if depth == M:
        print(' '.join(lis))
        return
    else:
        for _ in range(1, N+1):
            if str(_) not in lis:
                lis[depth] = str(_)
                permu(depth)

N, M = list(map(int,input().split()))
# permu([])
lis=[0 for _ in range(M)]
permu(-1)

