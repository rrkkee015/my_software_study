import sys
sys.stdin=open('input.txt','r')

testcases=int(input())
for tc in range(testcases):
    N=int(input())
    cnt=0
    lis=[]
    mat=[list(map(int,input().split())) for i in range(N)]
    result=''
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] != 0:
                y=i
                x=j
                cnt+=1
                while 0<=x<N-1 and mat[y][x+1]!=0:
                    x+=1
                while 0<=y<N-1 and mat[y+1][x]!=0:
                    y+=1
                for b in range(i,y+1):
                    for a in range(j,x+1):
                            mat[b][a]=0
                temp=[x-j+1,y-i+1,(x-j+1)*(y-i+1)]
                lis+=[temp]
    for i in range(len(lis)-1,0,-1):
        for j in range(0,i):
            if lis[j][2]>lis[j+1][2]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
            elif lis[j][2]==lis[j+1][2]:
                if lis[j][1]>lis[j+1][1]:
                    lis[j],lis[j+1]=lis[j+1],lis[j]
    for i in lis:
        result+= str(i[1])+' '+str(i[0])+' '
    print(f'#{tc+1} {cnt} {result}')







# import sys
# sys.stdin=open('input.txt','r')
#
#
# testcases=int(input())
# for tc in range(testcases):
#     N=int(input())
#     mat=[list(map(int,input().split())) for i in range(N)]
#     cnt=0
#     lis=[]
#     # print(mat)
#     for i in range(len(mat)):
#         for j in range(len(mat[0])):
#             if mat[i][j] != 0:
#                 y=i
#                 x=j
#                 cnt+=1
#                 while 0<=x<N-1 and mat[y][x+1]!=0:
#                     x+=1
#                 while 0<=y<N-1 and mat[y+1][x]!=0:
#                     y+=1
#                 for k in range(i,y+1):
#                     for z in range(j, x+1):
#                         mat[k][z]=0
#                 lis += [[x - j + 1, y - i + 1, 0]]
#     for i in lis:
#         i[2]=i[0]*i[1]
#     for i in range(len(lis)-1,0,-1):
#         for j in range(0,i):
#             if lis[j][2]>lis[j+1][2]:
#                 lis[j],lis[j+1]=lis[j+1],lis[j]
#             elif lis[j][2]==lis[j+1][2]:
#                 if lis[j][1]>lis[j+1][1]:
#                     lis[j],lis[j+1]=lis[j+1],lis[j]
#     result=''
#     for i in lis:
#         result+= str(i[1]) + ' ' + str(i[0]) + ' '
#     print(f'#{tc+1} {cnt} {result}')