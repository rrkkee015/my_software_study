inp=list(map(int,input().split()))
max_=max(inp)
history=[[0,0,0] for i in range(max_+1)]

for i in range(0,len(inp),2):
    P=inp[i]
    S=inp[i+1]
    if history[P][0]==0:
        history[P][0]=S
    elif history[P][0]!=0:
        history[P][1]=S
    history[S][2]=P
for i in history:
    print(i)

#1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13