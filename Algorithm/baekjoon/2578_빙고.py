mine=[list(map(int,input().split())) for _ in range(5)]
you=[]
for _ in range(5):
    you+=list(map(int,input().split()))

cnt=0
game=0
for k in you:
    cnt=0
    game+=1
    for a in range(5):
        for b in range(5):
            if mine[a][b]==k:
                mine[a][b]=0

    for i in range(5):
        for j in range(5):
            if mine[i][j]==0:
                continue
            else:
                break
        else:
            cnt+=1

    for i in range(5):
        for j in range(5):
            if mine[j][i]==0:
                continue
            else:
                break
        else:
            cnt+=1

    for i in range(5):
        if mine[i][i]==0:
            continue
        else:
            break
    else:
        cnt+=1

    for i in range(5):
        if mine[4-i][i]==0:
            continue
        else:
            break
    else:
        cnt+=1
    if cnt>=3:
        break
print(game)