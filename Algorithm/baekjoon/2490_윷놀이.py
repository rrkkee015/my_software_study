result=''
for i in range(3):
    cnt=0
    dggym=list(map(int,input().split()))
    for _ in dggym:
        if _==1:
            cnt+=1
    if cnt==4:
        result+='E'
    elif cnt==3:
        result+='A'
    elif cnt==2:
        result+='B'
    elif cnt==1:
        result+='C'
    else:
        result+='D'
for i in result:
    print(i)