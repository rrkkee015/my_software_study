people=int(input())
scores=[0]*(people+1)
for _ in range(people):
    num=list(map(int,input().split()))
    temp_result=[]
    max_=0
    for i in range(1<<len(num)):
        temp=[]
        for j in range(len(num)):
            if i & 1<<j:
                temp+=[num[j]]
        temp_result+=[temp]
    for __ in temp_result:
        if len(__)==3:
            if int(str(sum(__))[-1])>max_:
                max_=int(str(sum(__))[-1])
    scores[_+1]=max_
winner=[-1,-1]
for _ in range(1,len(scores)):
    if winner[0]<=scores[_]:
        winner[0]=scores[_]
        winner[1]=_
print(winner[1])