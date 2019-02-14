import sys
sys.stdin=open('input.txt','r')

# for tc in range(testcases):
#     V,E=tuple(map(int,input().split()))
#     matrix=[[0 for i in range(V+1)] for i in range(V+1)]
#     lis=list(map(int,input().split()))
#     for i in range(0, len(lis), 2):
#         matrix[lis[i+1]][lis[i]]=1
#         matrix[0][lis[i]]+=1
#     stack=[0 for i in range(V)]
#     visited=[False for i in range(V+1)]
#     visited[0]=True
#     result=''
#     while False in visited:
#         for i in range(len(matrix)):
#             if matrix[0][i] !=0 and visited[i]==False:
#                 S=i
#                 result+=str(S)+' '
#                 visited[S]=True
#                 matrix[0][S]-=1
#                 break
#         for j in range(len(matrix)):
#             if matrix[j][S]==1:
#                 matrix[j][S]=0
#     print(f'#{tc+1} {result}')

for tc in range(testcases):
    V,E=tuple(map(int,input().split()))
    matrix=[[0 for i in range(V+1)] for i in range(V+1)]
    lis=list(map(int,input().split()))
    for i in range(0, len(lis), 2):
        matrix[lis[i+1]][lis[i]]=1
        k = lis[i+1]
        matrix[0][k] += 1
    stack=[0 for i in range(V)]
    visited=[False for i in range(V+1)]
    visited[0]=True
    result=''
    while False in visited:
        for i in range(len(matrix)):
            if matrix[0][i]==0 and visited[i]==False:
                S=i
                result+=str(S)+' '
                visited[S]=True
                break
        for j in range(len(matrix)):
            if matrix[j][S]==1:
                matrix[j][S]=0
                matrix[0][j] -= 1
    print(f'#{tc+1} {result}')
