w,h=




























# dxdy=[1,1]
# w,h=list(map(int,input().split()))
# x,y=list(map(int,input().split()))
# s=(x,y)
# time=int(input())
# t=0
# while t!=time:
#     t+=1
#     if x+dxdy[0]<0 or x+dxdy[0]>w:
#         dxdy[0]*=-1
#     if y+dxdy[1]<0 or y+dxdy[1]>h:
#         dxdy[1]*=-1
#     x,y=[x+dxdy[0],y+dxdy[1]]
#     if s==(x,y) and dxdy==[1,1]:
#         break
# t=time%t
# if t!=0:
#     while t != 0:
#         t -= 1
#         if x + dxdy[0] < 0 or x + dxdy[0] > w:
#             dxdy[0] *= -1
#         if y + dxdy[1] < 0 or y + dxdy[1] > h:
#             dxdy[1] *= -1
#         x, y = [x + dxdy[0], y + dxdy[1]]
# print(x,y)