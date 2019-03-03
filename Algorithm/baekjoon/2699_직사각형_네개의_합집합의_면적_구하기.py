mat = [[0] * 101 for _ in range(101)]
for _ in range(4):
    cnt=0
    x1,y1,x2,y2=list(map(int,input().split()))
    for i in range(101):
        for j in range(101):
            if x1<=j<x2 and y1<=i<y2:
                mat[i][j]=1

for i in range(101):
    for j in range(101):
        if mat[i][j]!=0:
            cnt+=1
print(cnt)