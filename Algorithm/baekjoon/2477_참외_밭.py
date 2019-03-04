nums=int(input())
lis=[]
for _ in range(6):
    lis+=[list(map(int,input().split()))]
resultw=0
resulth=0
for i in range(len(lis)):
    if lis[i][0]==1 or lis[i][0]==2:
        if resultw<lis[i][1]:
            resultw=lis[i][1]
            minh=lis[i-3][1]
    if lis[i][0]==3 or lis[i][0]==4:
        if resulth<lis[i][1]:
            resulth=lis[i][1]
            minw=lis[i-3][1]
result=resultw*resulth-minw*minh
print(result*nums)