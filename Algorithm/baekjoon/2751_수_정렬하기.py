# def partition(lis, p, r): # lis : 파티션을 구분할 리스트, 배열의 시작점, 배열의 끝지점
#     x = lis[r] # lis의 제일 끝 지점
#     i = p - 1 # 배열 처음에서 -1
#     for j in range(p, r): # 배열의 시작점부터 끝 지점 앞에까지 왜냐면 x를 잡고 후두려 패는 거니까
#         if lis[j] <= x: # 배열의 끝지점인 x가 순회하는 값 lis[j]보다 크면
#             i+=1 # i도 j 따라서 같이 증가
#             lis[i], lis[j] = lis[j], lis[i] # 서로 교환 만약에 정렬된 배열이었으면 파티션이 안나눠지고 계속 제자리에서 스위칭했겠지
#                                             # 만약 x보다 큰 값이 나오면 j만 증가한다.
#     lis[i+1], lis[r] = lis[r], lis[i+1] # 파티션이 들어갈 위치를 정했으니 i+1 위치와 r의 위치를 바꾸고
#     return i + 1 # 새로운 pivot 값이 탄생한다.
#
# def quicksort(lis, s, g): # lis : 정렬할 배열, s : 배열의 시작점, g : 배열의 끝 지점
#     if s < g: # 시작점과 끝 점이 같을 땐, 배열 하나만 제자리에서 바꾸는 거니까 거기가 마지막임 # 왜 '<' 이거냐면 마지막 진짜 마지막에 pivot이 1로 들어온다면 두 번째 호출에서 p+1 = 2, g = 1 이 되어버려서 역전되는 경우가 있다.
#         p = partition(lis, s, g) # 중간 파티션을 나누고
#         quicksort(lis, s, p-1) # 피봇 기준 왼쪽
#         quicksort(lis, p+1, g) # 피봇 기준 오른쪽
#
# N = int(input())
# bs = [int(input()) for _ in range(N)]
# quicksort(bs,0,len(bs)-1) # 정렬할 배열, 배열의 시작점, 배열의 끝지점 (배열의 길이가 아니다.)
# for _ in bs:
#     print(_)

# 위는 퀵 정렬로 해결하려고 했던 문제다. 근데 퀵 정렬이 최악의 경우 O(N^2)이라서 그걸 처리를 못한다.
# 그래서 이 문제는 퀵 정렬이 좋지 않다.

# 병합 정렬로 풀어보자
# N = int(input())
# def merge_sort(lis):
#     if len(lis) == 1:
#         return lis
#     left = []
#     right = []
#     middle = len(lis)//2
#     for x in range(0, middle):
#         left.append(lis[x])
#     for x in range(middle, len(lis)):
#         right.append(lis[x])
#     left = merge_sort(left)
#     right = merge_sort(right)
#     return merge(left, right)
#
# def merge(l, r):
#     result=[]
#     while len(l) > 0 or len(r) > 0:
#         if len(l) > 0 and len(r) > 0:
#             if l[0] <= r[0]:
#                 result.append(l.pop(0))
#             else:
#                 result.append(r.pop(0))
#         elif len(l) > 0:
#             result.append(l.pop(0))
#         elif len(r) > 0:
#             result.append(r.pop(0))
#     return result
#
# lis = [int(input()) for _ in range(N)]
# re = merge_sort(lis)
# for _ in re:
#     print(_)

# 이것 마저 안된다

# 그냥 라이브러리 쓰자
N = int(input())
lis = [int(input()) for _ in range(N)]
lis = sorted(lis)
for _ in lis:
    print(_)