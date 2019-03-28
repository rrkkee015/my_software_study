import sys
sys.stdin = open('sample_input.txt','r')

def divide(lis, l):
    global cnt
    if len(lis) == 1:
        return lis
    elif len(lis) == 2:
        if lis[0] > lis[1]:
            cnt += 1
            lis[0],lis[1] = lis[1],lis[0]
        return lis
    cen = len(lis)//2
    left = lis[:cen]
    right = lis[cen:]
    left = divide(left, l//2)
    right = divide(right, l-l//2)
    result = [0] * l
    if left[-1] > right[-1]:
        cnt += 1
    i,j,k = 0,0,0
    while i < l//2 and j < l - l//2:
        if left[i] >= right[j]:
            result[k] = right[j]
            j += 1
        else:
            result[k] = left[i]
            i += 1
        k += 1
    while i < l//2:
        result[k] = left[i]
        i += 1
        k += 1
    while j < l - l//2:
        result[k] = right[j]
        j += 1
        k += 1
    return result

# 시간 초과
# def merge_sort(lis):
#     global cnt
#     if len(lis) > 1:
#         cen = len(lis) // 2
#         left = lis[:cen]
#         right = lis[cen:]
#
#         merge_sort(left)
#         merge_sort(right)
#
#         i,j,k = 0, 0, 0
#         if left[-1] > right[-1]:
#             cnt += 1
#         while i < len(left) and j < len(right):
#             if left[i] >= right[j]:
#                 lis[k] = right[j]
#                 j +=1
#             else:
#                 lis[k] = left[i]
#                 i+=1
#             k+=1
#         if i < len(left):
#             lis[k:k+len(left)] = left[i:]
#         if j < len(right):
#             lis[k:k+len(right)] = right[j:]
#         # while i < len(left):
#         #     lis[k] = left[i]
#         #     i += 1
#         #     k += 1
#         # while j < len(right):
#         #     lis[k] = right[j]
#         #     j += 1
#         #     k += 1
#     return lis

testcases = int(input())
for tc in range(testcases):
    N = int(input())
    li = list(map(int,input().split()))
    cnt = 0
    re = divide(li, N)
    print(f'#{tc+1} {re[N//2]} {cnt}')