# from itertools import combinations

# def combinations(idx,temp):
#     global cnt, result
#     if temp != [] and sum(temp)==S:
#         cnt+=1
#         return
#     elif idx==N:
#         return
#     else:
#         combinations(idx+1,temp[:])
#         temp.append(lis[idx])
#         combinations(idx+1,temp[:])

def jiphap(temp):
    global cnt
    if sum(temp)==S:
        cnt+=1
        return
    else:
        for i in lis:
            temp.append(i)
            jiphap(temp)
            temp.pop(i)

N,S = list(map(int,input().split()))
lis=list(map(int,input().split()))
cnt=0
visited=[False]*(N+1)
jiphap(visited)
print(cnt)

# 라이브러리 사용
# N,S = list(map(int,input().split()))
# lis=list(map(int,input().split()))
# cnt=0
# for _ in range(1,N+1):
#     result=combinations(lis, _)
#     for __ in result:
#         if sum(__) == S:
#             cnt+=1
# print(cnt)