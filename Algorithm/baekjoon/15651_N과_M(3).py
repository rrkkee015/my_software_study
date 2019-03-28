# def permutation(n, r):
#     if n == r:
#         print(lis)
#         return
#     else:
#         for _ in range(r,n+1):
#             lis[_-1],lis[r-1] = lis[r-1],lis[_-1]
#             permutation(n,r+1)
#             lis[_-1],lis[r-1] = lis[r-1],lis[_-1]
from itertools import permutations # 그냥순열
from itertools import product # 중복순열
N, M = list(map(int,input().split()))
lis = [str(_) for _ in range(1,N+1)]
for _ in list(product(lis, repeat=M)):
    print(' '.join(_))