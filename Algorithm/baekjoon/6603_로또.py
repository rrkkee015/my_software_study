from itertools import combinations

# 조합 문제가 아닐까 싶다.
# 라이브러리, 내가 직접짜기 2개를 해보자

# def permutation(_):
#     if len(_)==3:
#         print(_)
#         return
#     for i in lis:
#         if i not in _:
#             _.append(i)
#             permutation(_)
#             _.pop()

# def combination(_):
#     print(1)
#     global result
#     if len(_)==6:
#         sor=sorted(_)
#         if sor not in result:
#             result+=[sor]
#             return
#     for i in lis:
#         if visited[i]==False:
#             _.append(i)
#             visited[i]=True
#             combination(_)
#             _.pop()
#             visited[i]=False

# while True:
#     temp=list(map(int,input().split()))
#     if temp[0]==0:
#         break
#     else:
#         lis=temp[1:]
#         result=[]
#         visited=[False]*50
#         result=combinations(lis, 6)
#         for _ in list(result):
#             print(' '.join(str(x) for x in _))
#     print()

def combinations(idx, temp):
    global result
    if len(temp) == n:
        result.append(sorted(temp))
        return
    elif idx == len(num_list):
        return
    else:
        combinations(idx+1,temp[:])
        temp.append(num_list[idx])
        combinations(idx+1,temp[:])

while True:
    temp=list(map(int,input().split()))
    k=temp[0]
    if k==0:
        break
    else:
        num_list=temp[1:]
        num_list=num_list[::-1]
        n=6
        result=[]
        combinations(0,[])
        for i in sorted(result):
            print(' '.join(str(x) for x in i))
    print()