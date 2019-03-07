N=int(input())
mat=[[0]*101 for _ in range(101)]
cnt=1
for _ in range(N):
    x,y,w,h=list(map(int,input().split()))
    for i in range(101):
        for j in range(101):
            if i==y and j==x:
                for p in range(i,i+h):
                    for q in range(j,j+w):
                        mat[p][q]=cnt
    cnt += 1
for o in range(1,cnt):
    result=0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]==o:
                result+=1
    print(result)