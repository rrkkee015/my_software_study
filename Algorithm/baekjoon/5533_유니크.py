def check(lis):
    for _ in range(len(lis)):
        temp=lis[_]
        for __ in range(_+1,len(lis)):
            if temp==lis[__]:
                lis[_]=0
                lis[__]=0
    return lis

N=int(input())
scores=[list(map(int,input().split())) for _ in range(N)]
fg=[0]*N
sg=[0]*N
tg=[0]*N
for j in range(3):
    for i in range(N):
        if j==0:
            fg[i]=scores[i][j]
        elif j==1:
            sg[i]=scores[i][j]
        elif j==2:
            tg[i]=scores[i][j]
fg=check(fg)
sg=check(sg)
tg=check(tg)
for _ in range(N):
    print(fg[_]+sg[_]+tg[_])