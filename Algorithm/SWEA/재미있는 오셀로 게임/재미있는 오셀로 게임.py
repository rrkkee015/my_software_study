import sys
sys.stdin=open('sample_input(1).txt','r')
testcases=int(input())
for tc in range(testcases):
    N,M=list(map(int,input().split()))
    mat=[[0]*N for _ in range(N)]
    mat[N//2][N//2]=2
    mat[N//2-1][N//2-1]=2
    mat[N//2][N//2-1]=1
    mat[N//2-1][N//2]=1
    for _ in range(M):
        atkx,atky,color=list(map(int,input().split()))
        mat[atky-1][atkx-1]=color
        for __ in range(atkx,N): #오른쪽 탐색
            if mat[atky - 1][__] == 0:
                break
            if color==1:
                if mat[atky-1][__]==1:
                    for i in range(atkx-1,__):
                        mat[atky-1][i]=1
                    break
            elif color==2:
                if mat[atky-1][__]==2:
                    for i in range(atkx-1,__):
                        mat[atky-1][i]=2
                    break
        for __ in range(atkx-2,-1,-1): #왼쪽 탐색
            if mat[atky - 1][__] == 0:
                break
            if color==1:
                if mat[atky-1][__]==1:
                    for i in range(atkx-1,__,-1):
                        mat[atky-1][i]=1
                    break
            elif color == 2:
                if mat[atky-1][__]==2:
                    for i in range(atkx-1,__,-1):
                        mat[atky-1][i]=2
                    break
        for __ in range(atky,len(mat)): #아래쪽 탐색
            if mat[__][atkx - 1] == 0:
                break
            if color==1:
                if mat[__][atkx-1]==1:
                    for i in range(atky-1,__):
                        mat[i][atkx-1]=1
                    break
            elif color == 2:
                if mat[__][atkx-1]==2:
                    for i in range(atky-1,__):
                        mat[i][atkx-1]=2
                    break
        for __ in range(atky-2, -1, -1): #위쪽 탐색
            if mat[__][atkx - 1] == 0:
                break
            if color==1:
                if mat[__][atkx-1]==1:
                    for i in range(atky-1,__,-1):
                        mat[i][atkx-1]=1
                    break
            elif color == 2:
                if mat[__][atkx-1]==2:
                    for i in range(atky-1,__,-1):
                        mat[i][atkx-1]=2
                    break
        i=atky-1
        j=atkx-1
        cnt=0
        p = atky - 1
        q = atkx - 1
        for __ in range(len(mat)): #대각선 오른쪽 위
            i-=1
            j+=1
            if 0 <= i < N and 0 <= j < N:
                if mat[i][j] == 0:
                    break
                cnt += 1
                if color==1:
                    if mat[i][j]==1:
                        for ___ in range(cnt-1):
                            p-=1
                            q+=1
                            if 0 <= p < N and 0 <= q < N:
                                mat[p][q] = 1
                        break
                elif color == 2:
                    if mat[i][j]==2:
                        for ___ in range(cnt-1):
                            p-=1
                            q+=1
                            if 0 <= p < N and 0 <= q < N:
                                mat[p][q] = 2
                        break
        i = atky - 1
        j = atkx - 1
        cnt = 0
        p = atky - 1
        q = atkx - 1
        for __ in range(len(mat)):  # 대각선 오른쪽 아래
            i += 1
            j += 1
            if 0 <= i < N and 0 <= j < N:
                if mat[i][j] == 0:
                    break
                cnt += 1
                if color == 1:
                    if mat[i][j] == 1:
                        for ___ in range(cnt-1):
                            p += 1
                            q += 1
                            if 0 <= p < N and 0 <= q < N:
                                mat[p][q] = 1
                        break
                elif color == 2:
                    if mat[i][j] == 2:
                        for ___ in range(cnt-1):
                            p += 1
                            q += 1
                            if 0 <= p < N and 0 <= q < N:
                                mat[p][q] = 2
                        break
        i = atky - 1
        j = atkx - 1
        cnt = 0
        p = atky - 1
        q = atkx - 1
        for __ in range(len(mat)):  # 대각선 왼쪽 아래
            i += 1
            j -= 1
            if 0 <= i < N and 0 <= j < N:
                if mat[i][j] == 0:
                    break
                cnt += 1
                if color == 1:
                    if mat[i][j] == 1:
                        for ___ in range(cnt-1):
                            p += 1
                            q -= 1
                            if 0 <= p < N and 0 <= q < N:
                                mat[p][q] = 1
                        break
                elif color == 2:
                    if mat[i][j] == 2:
                        for ___ in range(cnt-1):
                            p += 1
                            q -= 1
                            if 0 <= p < N and 0 <= q < N:
                                mat[p][q] = 2
                        break
        i = atky - 1
        j = atkx - 1
        cnt = 0
        p = atky - 1
        q = atkx - 1
        for __ in range(len(mat)):  # 대각선 왼쪽 위
            i -= 1
            j -= 1
            if 0 <= i < N and 0 <= j < N:
                if mat[i][j] == 0:
                    break
                cnt += 1
                if color == 1:
                    if mat[i][j] == 1:
                        for ___ in range(cnt-1):
                            p -= 1
                            q -= 1
                            if 0 <= p < N and 0 <= q < N:
                                mat[p][q] = 1
                        break
                elif color == 2:
                    if mat[i][j] == 2:
                        for ___ in range(cnt-1):
                            p -= 1
                            q -= 1
                            if 0 <= p < N and 0 <= q < N:
                                mat[p][q] = 2
                        break
        for i in mat:
            print(i)
        print()
    wcnt=0
    bcnt=0
    for i in range(N):
        for j in range(N):
            if mat[i][j]==1:
                bcnt+=1
            elif mat[i][j]==2:
                wcnt+=1
    print('#{} {} {}'.format(tc+1,bcnt,wcnt))