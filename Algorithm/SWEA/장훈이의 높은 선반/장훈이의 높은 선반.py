import sys
sys.stdin = open('input.txt','r')

def top(d,s):
    global m
    d+=1
    if B<=s<m:
        m=s
        return
    if d== N:return
    else:
        top(d,s)
        top(d,s+h[d])
tc = int(input())
for _ in range(tc):
    N,B=list(map(int,input().split()))
    h=list(map(int,input().split()))
    m=sum(h)
    top(-1,0)
    print(f'#{_+1} {m-B}')

# def top(n, r):
#     if r == 0:
#         result.append(temp[:])
#     elif n < r:
#         return
#     else:
#         temp[r-1] = height[n-1]
#         top(n-1,r-1)
#         top(n-1,r)
# 
# testcases = int(input())
# for tc in range(testcases):
#     N, B = list(map(int,input().split()))
#     height = list(map(int,input().split()))
#     result = []
#     max_ = sum(height)
#     for _ in range(1, N + 1):
#         temp = [0] * _
#         top(len(height), len(temp))
#     for _ in result:
#         if sum(_) < B:
#             continue
#         if B <= sum(_) and sum(_) < max_:
#             max_ = sum(_)
#     print(f'#{tc+1} {max_-B}')
# 조합을 사용

# def top(sum_):
#     global max_
#     if max_ > sum_ >= B:
#         max_ = sum_
#     elif max_ < sum_:
#         return
#     elif sum_ == B:
#         max_ = sum_
#         return
#     else :
#         for _ in range(len(visited)):
#             if visited[_] == False:
#                 visited[_] = True
#                 top(sum_ + height[_])
#                 visited[_] = False
# # 이 코드 순열이다. 이렇게 풀면 안됨

























# testcases = int(input())
# def top(sum_):
#     global max_
#     if sum_ < B:
#         return
#     if max_ - B == 0:
#         return
#     else:
#         for _ in range(len(height)):
#             if visited[_] == False:
#                 visited[_] = True
#                 if B <= sum_ - height[_] < max_:
#                     max_ = sum_ - height[_]
#                 top(sum_ - height[_])
#                 visited[_] = False
#
# for tc in range(testcases):
#     N, B = list(map(int,input().split()))
#     height = list(map(int,input().split()))
#     visited = [False] * N
#     result = []
#     max_ = sum(height)
#     top(sum(height))
#     print(f'#{tc+1} {max_ - B}')