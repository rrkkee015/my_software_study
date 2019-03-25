def perm(n,k):
    if k == n:
        print(arr)
    else:
        for i in range(k,n):
            arr[k],arr[i]=arr[i],arr[k]
            perm(n,k+1)
            arr[k],arr[i]=arr[i],arr[k]
arr=[1,2,3]
perm(3,0)

# def perm(n, k): # 배열의 길이, k = 0 부터 시작
#     if k == n:
#         print(arr)
#     else:
#         for i in range(k, n):
#             arr[k], arr[i] = arr[i], arr[k]
#             perm(n, k+1)
#             arr[k], arr[i] = arr[i], arr[k]
#
# arr = [1,2,3,4,5]
# perm(5, 0)
#
# arr='ABC'
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             print(arr[i],arr[j],arr[k]) # 이렇게하면 중복순열
#
# for i in range(3):
#     for j in range(3):
#         if j==i:
#             continue
#         for k in range(3):
#             if k ==i or k ==j:
#                 continue
#             else:
#                 print(arr[i],arr[j],arr[k])
#
# def permutation(lis):
#     if len(temp)==3:
#         print(temp)
#         return
#     else:
#         for _ in range(len(arr)):
#             if arr[_] not in temp:
#                 temp.append(arr[_])
#                 permutation(temp)
#                 temp.pop()
#
# temp=[]
# arr=['A','B','C']
# permutation(arr)
#
# order = [0] * 3 # 요소들의 인덱스를 저장
# arr = 'ABC'
#
# def perm(k, n): # k : 지금까지 선택(노드의 높이), n : 전체 선택(트리의 높이)
#     if k == n:
#         return
#     else:
#         used = [False] * n # 중복 안되게
#         for i in range(k):
#             used[order[i]] = True
#         for i in range(n):
#             if used[i]:
#                 continue
#             else:
#                 order[k] = i
#                 perm(k+1, n)
#
# perm(0, 3)
#
# used = [False] * 3
# def perm(k, n): # k : 지금까지 선택(노드의 높이), n : 전체 선택(트리의 높이)
#     if k == n:
#         print(order)
#         return
#     else:
#         for i in range(n):
#             if used[i]:
#                 continue
#             else:
#                 order[k] = i
#                 used[i] = True
#                 perm(k+1, n)
#                 used[i] = False
# perm(0, 3)
#
# # used를 매개변수로 만들기
# def perm(k, n, used): # k : 지금까지 선택(노드의 높이), n : 전체 선택(트리의 높이)
#     if k == n:
#         print(order)
#         return
#     else:
#         for i in range(n):
#             if used & (1<<i):
#                 order[k]=i
#                 perm(k+1,n,used | (1<<i))
#
# perm(0, 3, 0)
#
# # N=Queen 문제가 순열이다.

# 조합 재귀
def combi(n,r):
    if r == 0:
        print(tr)
    elif n < r :
        return
    else:
        tr[r-1] = an[n-1]
        combi(n-1, r-1)
        combi(n-1, r)
an = [1,2,3,4,5]
tr = [0 for _ in range(3)]
combi(len(an), len(tr))