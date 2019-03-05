N=int(input())
swi=[0]*(N+1)
swi[0]='-'
temp=list(map(int,input().split()))
for i in range(1,len(swi)):
    swi[i]=temp[i-1]
stus=int(input())
for _ in range(stus):
    stu=list(map(int,input().split()))
    if stu[0]==1: #남자일 때
        for i in range(len(swi)):
            if i%stu[1]==0 and i != 0:
                if swi[i]==0:
                    swi[i]=1
                else:
                    swi[i]=0
    else: #여자일 때
        s=stu[1]
        g=stu[1]
        while 0<=s<N+1 and 0<=g<N+1 and swi[s]==swi[g]: #범위 조심
            s-=1
            g+=1
        for i in range(s+1,g):
            if swi[i] == 0:
                swi[i] = 1
            else:
                swi[i] = 0
cnt=1
for _ in swi[1:]:
    if cnt==21:
        print()
        cnt=1
    print(_,end=' ')
    cnt+=1