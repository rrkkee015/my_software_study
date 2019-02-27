import sys
sys.stdin=open('input.txt','r')

# testcases=int(input())
# for tc in range(testcases):
#     print(f'#{tc+1}')
#     N=int(input())
#     mat=[list(map(int,input().split())) for i in range(N)]
#     result=[]
#     total_result=[]
#     #90도
#     for  j in range(N):
#         temp=[]
#         for i in range(N-1,-1,-1):
#             temp+=[mat[i][j]]
#         result+=[temp]
#     total_result+=result
#     result=[]
#     #180도
#     for i in range(N-1,-1,-1):
#         temp=[]
#         for j in range(N-1,-1,-1):
#             temp+=[mat[i][j]]
#         result+=[temp]
#     total_result+=result
#     result=[]
#     #270도
#     for j in range(N-1,-1,-1):
#         temp=[]
#         for i in range(N):
#             temp+=[mat[i][j]]
#         result+=[temp]
#     total_result+=result
#     #전체 출력
#     for i in range(N):
#         gu = ''
#         baek = ''
#         ebaek = ''
#         for j in range(N):
#             gu+=str(total_result[i][j])
#             baek+=str(total_result[i+N][j])
#             ebaek+=str(total_result[i+2*N][j])
#         print(gu+' '+baek+' '+ebaek)
#     if i !=N-1:
#         print()

#홍두형
testcases=int(input())
for tc in range(testcases):
    print(f'#{tc+1}')
    N=int(input())
    mat=[list(map(int,input().split())) for i in range(N)]
    for i in range(N):
        a,b,c=('','','')
        for j in range(N):
            a+=str(mat[N-1-j][i])
            b+=str(mat[N-1-i][N-1-j])
            c+=str(mat[j][N-1-i])
        print(f'{a} {b} {c}')