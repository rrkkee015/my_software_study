import sys
sys.stdin=open('input.txt','r')
# for tc in range(10):
#     tc = int(input())
#     matrix= [list(map(int,input().split())) for i in range(100)]
#     data = [[0 for j in range(102)] for k in range(101)]
#     #틀 만들기
#     for i in range(100):
#         for j in range(1,101):
#             data[i][j]=matrix[i][j-1]
#     #틀 만들기 끝
#     # #경계선 만들기 시작
#     # for j in range(102):
#     #     data[100][j]=99
#     # for i in range(101):
#     #     data[i][0]=99
#     #     data[i][101]=99
#     # # 경계선 만들기 끝
#     # 사다리 시작
#     for j in range(1,101):
#         x=j
#         for i in range(0,100):
#             if data[0][x]==0:
#                 break
#             if data[i][x+1]==1: #오른쪽 검사
#                 while data[i][x+1]==1:
#                     x+=1
#             elif data[i][x-1]==1: #왼쪽 검사
#                 while data[i][x-1]==1:
#                     x-=1
#             if data[i][x]==2:
#                 print(f'#{str(tc)} {j-1}')
#                 break
for tc in range(10):
    tc=int(input())
    matrix=[list(map(int,input().split())) for i in range(100)]
    for i in range(len(matrix[99])):
        if matrix[99][i]==2:
            num=i
    for k in range(99,-1,-1):
        if num<99 and matrix[k][num+1]==1:
            while matrix[k][num+1]==1:
                if num+1==99:
                    num+=1
                    break
                num=num+1
        elif num>0 and matrix[k][num-1]==1:
            while matrix[k][num-1]==1:
                if num-1==0:
                    num-=1
                    break
                num=num-1
    print(num)