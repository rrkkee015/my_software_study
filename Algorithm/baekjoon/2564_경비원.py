w,h=list(map(int,input().split()))
stores=int(input())
sp=[]
result=0
for i in range(stores):
    sp+=[list(map(int,input().split()))]
dongun=list(map(int,input().split()))
if dongun[0] ==1: #북쪽
    for _ in sp:
        if _[0] == 1: #같으면 절댓값
            result+=abs(_[1] - dongun[1])
        elif _[0] == 2: #남쪽
            a=h+dongun[1]+_[1] #반시계
            b=h+w-dongun[1]+w-_[1] #시계
            if a<b:
                result+=a
            else:
                result+=b
        elif _[0] == 3: #서쪽
            result+=dongun[1]+_[1]
        elif _[0] == 4: #동쪽
            result+=w-dongun[1]+_[1]
if dongun[0]==2: #남쪽
    for _ in sp:
        if _[0]==1: #북쪽
            a=h+dongun[1]+_[1] #시계
            b=h+(w-dongun[1])+(w-_[1]) #반시계
            if a<b:
                result+=a
            else:
                result+=b
        elif _[0]==2: #같으면 절댓값
            result+=abs(_[1]-dongun[1])
        elif _[0]==3: #서쪽
            result+=dongun[1]+(h-_[1])
        elif _[0]==4: #동쪽
            result+=w-dongun[1]+h-_[1]
if dongun[0] == 3: #서쪽
    for _ in sp:
        if _[0] == 1: #북쪽
            result+=dongun[1]+_[1]
        elif _[0]==2: #남쪽
            result+=h-dongun[1]+_[1]
        elif _[0] == 3: #같으면 절댓값
            result+=abs(_[1]-dongun[1])
        elif _[0]==4: #동쪽
            a=dongun[1]+w+_[1] #시계
            b=h-dongun[1]+w+h-_[1] #반시계
            if a<b:
                result+=a
            else:
                result+=b
if dongun[0] == 4: #동쪽
    for _ in sp:
        if _[0]==1: #북쪽
            result+=dongun[1]+w-_[1]
        elif _[0]==2: #남쪽
            result+=h-dongun[1]+w-_[1]
        elif _[0]==3: #서쪽
            a=dongun[1]+w+_[1] #반시계
            b=h-dongun[1]+w+h-_[1] #시계
            if a<b:
                result+=a
            else:
                result+=b
        elif _[0] == 4: #같으면 절댓값
            result+=abs(_[1]-dongun[1])
print(result)