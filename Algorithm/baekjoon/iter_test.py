# from itertools import combinations
#
# while True:
#     temp=list(map(int,input().split()))
#     k=temp[0]
#     if k==0:
#         break
#     else:
#         lis=temp[1:]
#         result=combinations(lis,6)
#         for _ in result:
#             print(' '.join(str(x) for x in _))
#     print()

# def combinations(idx, temp):
#     global result
#     if len(temp) >= n:
#         result.append(sorted(temp))
#         return
#     elif idx == len(num_list):
#         return
#     else:
#         combinations(idx+1,temp)
#         temp.append(num_list[idx])
#         combinations(idx+1,temp)
#
# while True:
#     temp=list(map(int,input().split()))
#     k=temp[0]
#     if k==0:
#         break
#     else:
#         num_list=temp[1:]
#         num_list=num_list[::-1]
#         n=6
#         result=[]
#         combinations(0,[])
#         for i in sorted(result):
#             print(' '.join(str(x) for x in i))
#     print()


import itertools

li = [0, 1, 2, 3]
print(list(itertools.permutations(li,2)))
print(list(itertools.product(li, repeat=4)))
print(list(itertools.combinations(li, 3)))
print(list(itertools.combinations_with_replacement(li, 3)))