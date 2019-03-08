import sys
sys.stdin=open('s_input.txt','r')

testcases=int(input())

for tc in range(testcases):
    print('#{}'.format(tc+1))
    N,S = list(map(str,input().split()))
    N=int(N)
    mat=[list(map(int,input().split())) for _ in range(N)]
    if S=='up':
        for j in range(N):
            for i in range(N):
                if mat[i][j]!=0:
                    top=i
                    while top+1 != N:
                        top=top+1
                        if mat[top][j]==0:
                            continue
                        elif mat[top][j]==mat[i][j]:
                            mat[i][j]=mat[i][j]*2
                            mat[top][j]=0
                            break
                        elif mat[top][j]!=mat[i][j]:
                            if mat[top][j]!=0:
                                break
                            else:
                                mat[i+1][j]=mat[top][j]
                                mat[top][j]=0
                            break
        for j in range(N):
            for i in range(N):
                if mat[i][j]==0:
                    top=i
                    while top+1 !=N:
                        top=top+1
                        if mat[top][j]==0:
                            continue
                        else:
                            mat[i][j]=mat[top][j]
                            mat[top][j]=0
                            break
    if S=='down':
        for j in range(N):
            for i in range(N-1,-1,-1):
                if mat[i][j]!=0:
                    top=i
                    while top-1 != -1:
                        top=top-1
                        if mat[top][j]==0:
                            continue
                        elif mat[top][j]==mat[i][j]:
                            mat[i][j]=mat[i][j]*2
                            mat[top][j]=0
                            break
                        elif mat[top][j]!=mat[i][j]:
                            if mat[top][j]!=0:
                                break
                            else:
                                mat[i-1][j]=mat[top][j]
                                mat[top][j]=0
                            break
        for j in range(N):
            for i in range(N-1,-1,-1):
                if mat[i][j]==0:
                    top=i
                    while top-1 != -1:
                        top=top-1
                        if mat[top][j]==0:
                            continue
                        else:
                            mat[i][j]=mat[top][j]
                            mat[top][j]=0
                            break
    if S=='left':
        for i in range(N):
            for j in range(N):
                if mat[i][j]!=0:
                    top=j
                    while top+1 != N:
                        top=top+1
                        if mat[i][top]==0:
                            continue
                        elif mat[i][top]==mat[i][j]:
                            mat[i][j]=mat[i][j]*2
                            mat[i][top]=0
                            break
                        elif mat[i][top]!=mat[i][j]:
                            if mat[i][top]!=0:
                                break
                            else:
                                mat[i][j+1]=mat[i][top]
                                mat[i][top]=0
                            break
        for i in range(N):
            for j in range(N):
                if mat[i][j]==0:
                    top=j
                    while top+1 !=N:
                        top=top+1
                        if mat[i][top]==0:
                            continue
                        else:
                            mat[i][j]=mat[i][top]
                            mat[i][top]=0
                            break
    if S=='right':
        for i in range(N):
            for j in range(N-1,-1,-1):
                if mat[i][j]!=0:
                    top=j
                    while top-1 != -1:
                        top=top-1
                        if mat[i][top]==0:
                            continue
                        elif mat[i][top]==mat[i][j]:
                            mat[i][j]=mat[i][j]*2
                            mat[i][top]=0
                            break
                        elif mat[i][top]!=mat[i][j]:
                            if mat[i][top]!=0:
                                break
                            else:
                                mat[i][j-1]=mat[i][top]
                                mat[i][top]=0
                            break
        for i in range(N):
            for j in range(N-1,-1,-1):
                if mat[i][j]==0:
                    top=j
                    while top-1 !=-1:
                        top=top-1
                        if mat[i][top]==0:
                            continue
                        else:
                            mat[i][j]=mat[i][top]
                            mat[i][top]=0
                            break
    for i in mat:
        for j in i:
            print(j,end=' ')
        print()