# N=int(input())
# cnt=0
# roma=[0,0,0,0]
# nums=[1,5,10,50]
# visited=[]
# for a in range(N+1):
#     roma[0]=a
#     if sum(roma)==N and nums[3]*d+nums[2]*c+nums[1]*b+nums[0]*a not in visited:
#         cnt+=1
#         roma[0]=0
#         visited.append(nums[3]*d+nums[2]*c+nums[1]*b+nums[0]*a)
#         continue
#     for b in range(N+1):
#         roma[1]=b
#         if sum(roma)==N and nums[3]*d+nums[2]*c+nums[1]*b+nums[0]*a not in visited:
#             cnt+=1
#             roma[1]=0
#             visited.append(nums[3]*d+nums[2]*c+nums[1]*b+nums[0]*a)
#             continue
#         for c in range(N+1):
#             roma[2]=c
#             if sum(roma)==N and nums[3]*d+nums[2]*c+nums[1]*b+nums[0]*a not in visited:
#                 cnt+=1
#                 roma[2]=0
#                 visited.append(nums[3]*d+nums[2]*c+nums[1]*b+nums[0]*a)
#                 continue
#             for d in range(N+1):
#                 roma[3]=d
#                 if sum(roma)==N and nums[3]*d+nums[2]*c+nums[1]*b+nums[0]*a not in visited:
#                     cnt+=1
#                     roma[3]=0
#                     visited.append(nums[3]*d+nums[2]*c+nums[1]*b+nums[0]*a)
#                     continue
# print(cnt)

import itertools

N = int(input())
lis = [1, 5, 10, 50]
result = {}
for _ in itertools.combinations_with_replacement(lis, N):
    if result.get(sum(_)) == None:
        result[sum(_)] = 1
    else:
        continue
print(len(result))