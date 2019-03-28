# def stair(lis, n):
#     global max_
#     if len(lis) >= 3 and lis[-1] - lis[-2] == 1 and lis[-2] - lis[-3] == 1:
#         pass
#     elif n == N: # 저장하고 하는 것보다 받자마자 연산하는것이 메모리에 좋다.
#         # re.append(lis[:])
#         temp = 0
#         for _ in lis[:]:
#             temp += sc_st[_]
#         if max_ < temp:
#             max_ = temp
#     elif n > N:
#         pass
#     else:
#         for _ in range(1, 3):
#             tem = lis[:]
#             tem.append(n+_)
#             stair(tem[:], n+_)
#
# N = int(input())
# sc_st = [0]
# for _ in range(N):
#     sc_st.append(int(input()))
# # re = []
# max_ = 0
# stair([], 0)
# # for _ in re:
# #     temp = 0
# #     for i in _:
# #         temp += sc_st[i]
# #     if max_ < temp:
# #         max_ = temp
# print(max_)

# 시간초과, 메모리초과 원투 펀치

def stair(n):
    n+=1
    if n > N:
        return
    else:
        to[n] = max(sc[n] + to[n-2], sc[n] + sc[n-1] + to[n-3])
        stair(n)

N = int(input())
sc = [0]
for _ in range(N):
    sc.append(int(input()))
to =[0 for _ in range(N+1)]
stair(0)
print(to[-1])