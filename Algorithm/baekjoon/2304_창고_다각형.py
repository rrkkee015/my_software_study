N=int(input())
wh=[0]*1001
for _ in range(N):
    i,v=list(map(int,input().split()))
    wh[i]=v
max_=max(wh)
cnt=0
temp=0
result=0
for _ in wh:
    if _>temp:
        result+=temp*cnt
        temp=_
        cnt=1
    else:
        cnt+=1
temp=0
cnt=0
for _ in range(len(wh)-1,-1,-1):
    if wh[_]>=temp:
        result+=temp*cnt
        temp=wh[_]
        cnt=1
    else:
        cnt+=1
print(result+max_)