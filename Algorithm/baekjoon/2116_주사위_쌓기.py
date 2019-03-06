dices=int(input())
lis=[list(map(int,input().split())) for _ in range(dices)]
max_=0
for _ in range(1,7):
    top=_
    result=0
    for dice in lis:
        for k in range(len(dice)):
            if dice[k]==top:
                if k==0 or k==5:
                    result+=max([dice[1],dice[3],dice[2],dice[4]])
                    if k==0:
                        top=dice[5]
                    elif k==5:
                        top=dice[0]
                    break
                if k==1 or k==3:
                    result+=max([dice[2],dice[5],dice[0],dice[4]])
                    if k==1:
                        top=dice[3]
                    elif k==3:
                        top=dice[1]
                    break
                if k==2 or k==4:
                    result+=max([dice[0],dice[3],dice[5],dice[1]])
                    if k==2:
                        top=dice[4]
                    elif k==4:
                        top=dice[2]
                    break
    if max_<result:
        max_=result
print(max_)