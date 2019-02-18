# N=int(input())
# A=[int(input()) for i in range(N)]
# B=[0]*10000
# C=[0]*N
#
# for i in range(len(A)):
#     B[A[i]]+=1
#
# for k in range(1,len(B)):
#     B[k]=B[k]+B[k-1]
#
# for j in range(len(C)-1,-1,-1):
#     C[B[A[j]]-1]=A[j]
#     B[A[j]]-=1
#
# print(B)
# for i in C:
#     print(i)

import sys

# N=int(input())
# NUM=[0]*10001
# for i in range(N):
#     NUM[int(sys.stdin.readline())]+=1
#
# for i in range(len(NUM)):
#     if NUM[i]!=0:
#         for c in range(NUM[i]):
#             print(i)
# dic={}
N=int(input())
# for i in range(N):
#     a=int(input())
#     if a not in dic:
#         dic[a]=1
#     else:
#         dic[a]+=1
# for key,value in sorted(dic.items()):
#     for i in range(value):
#         print(key)

result=[0]*10001
for i in range(N):
    result[int(sys.stdin.readline())]+=1
for k in range(len(result)):
    print(f'{k}\n'* result[k], end='')