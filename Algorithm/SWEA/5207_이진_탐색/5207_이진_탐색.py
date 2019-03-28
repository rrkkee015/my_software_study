import sys
sys.stdin = open('sample_input.txt','r')

def find(l, r, target, TF):
    global cnt, tl, tr
    m = (l + r) // 2
    if list_A[m] == target:
        cnt += 1
        return
    else:
        if list_A[m] < target:
            if TF[0] == True:
                return
            else:
                l = m + 1
                tl += 1
                TF = [True,False]
                find(l, r, target, TF)
        elif target < list_A[m]:
            if TF[1] == True:
                return
            else:
                r = m - 1
                tr += 1
                TF = [False,True]
                find(l, r, target, TF)

testcases = int(input())
for tc in range(testcases):
    A, B = list(map(int,input().split()))
    list_A = sorted(list(map(int,input().split())))
    list_B = list(map(int,input().split()))
    cnt = 0
    for _ in list_B:
        tr = 0
        tl = 0
        if _ in list_A:
            m = (A-1)//2
            if list_A[m] == _:
                cnt += 1
            else:
                if list_A[m] < _:
                    l = m + 1
                    tl += 1
                    find(l, A-1, _, [True,False])
                elif _ < list_A[m]:
                    r = m - 1
                    tr += 1
                    find(0, r, _, [False,True])
    print(f'#{tc+1} {cnt}')

# 이진 탐색은 굳이 재귀함수를 돌릴 필요가 없다고 합니다.

# while low <= high:
#     m = (low + high) // 2
#     if A[m] == num:
#         ans += 1
#         return
#     elif num > A[m] and chk != 'r':
#         chk = 'r'
#         low = m + 1
#     elif num < A[m] and chk != 'l':
#         chk = 'l'
#         high = m - 1
#     else:
#         return