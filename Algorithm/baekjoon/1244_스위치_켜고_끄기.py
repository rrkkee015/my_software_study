N=int(input())
status=list(map(int,input().split()))
status.insert(0,99999)
stus=int(input())

for _ in range(stus):
    swi=list(map(int,input().split()))
    if swi[0]==1:
        for _ in range(N+1):
            if _%swi[1]==0:
                if status[_]==0:
                    status[_]=1
                elif status[_]==1:
                    status[_]=0
    if swi[0]==2:
        s,g=(swi[1],swi[1])
        if status[s]==1:
            status[s]=0
        elif status[s]==0:
            status[s]=1
        while 0<s-1 and g+1<=N and status[s-1]==status[g+1]:
            s-=1
            g+=1
            if status[s]==1:
                status[s]=0
            elif status[s]==0:
                status[s]=1
            if status[g]==1:
                status[g]=0
            elif status[g]==0:
                status[g]=1
cnt=0
for i in range(len(status)):
    if i !=0:
        print(status[i], end=' ')
    if cnt==20:
        print()
        cnt=0
    cnt += 1
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# N=int(input())
# swi=[0]*(N+1)
# swi[0]='-'
# temp=list(map(int,input().split()))
# for i in range(1,len(swi)):
#     swi[i]=temp[i-1]
# stus=int(input())
# for _ in range(stus):
#     stu=list(map(int,input().split()))
#     if stu[0]==1: #남자일 때
#         for i in range(len(swi)):
#             if i%stu[1]==0 and i != 0:
#                 if swi[i]==0:
#                     swi[i]=1
#                 else:
#                     swi[i]=0
#     else: #여자일 때
#         s=stu[1]
#         g=stu[1]
#         while 0<=s<N+1 and 0<=g<N+1 and swi[s]==swi[g]: #범위 조심
#             s-=1
#             g+=1
#         for i in range(s+1,g):
#             if swi[i] == 0:
#                 swi[i] = 1
#             else:
#                 swi[i] = 0
# cnt=1
# for _ in swi[1:]:
#     if cnt==21:
#         print()
#         cnt=1
#     print(_,end=' ')
#     cnt+=1