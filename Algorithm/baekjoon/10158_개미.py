w,h=list(map(int,input().split()))
p,q=list(map(int,input().split()))
sx,sy=p,q
cycle=[0,0]
i,j=1,1
cnt=0
cyx=0
cyy=0

while True:
    cnt+=1
    sx+=i
    if sx==0 or sx==w:
        i*=-1
    if sx==p:
        if cyx==1:
            cycle[0]=cnt
            break
        cyx+=1

cnt=0

while True:
    cnt+=1
    sy+=j
    if sy==0 or sy==h:
        j*=-1
    if sy==q:
        if cyy==1:
            cycle[1]=cnt
            break
        cyy+=1

time=int(input())
cycle=[time%cycle[0],time%cycle[1]]
cnt=0
i=1

while True:
    if cnt==cycle[0]:
        break
    cnt+=1
    p+=i
    if p==0 or p==w:
        i*=-1
cnt=0
i=1

while True:
    if cnt==cycle[1]:
        break
    cnt+=1
    q+=i
    if q==0 or q==h:
        i*=-1
print(p,q)