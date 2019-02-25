front=-1
rear=-1
total=20
Q=[0]*100000
idx=0
while True:
    new_sn=[idx+1,0]
    rear+=1
    Q[rear]=new_sn
    front+=1
    total-=Q[front][1]+1
    if total<=0:
        print(Q[front][0])
        break
    else:
        rear+=1
        Q[rear]=[Q[front][0],Q[front][1]+1]
        idx+=1