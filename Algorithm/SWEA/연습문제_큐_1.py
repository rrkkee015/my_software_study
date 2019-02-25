lis=[0]*3
rear=-1
front=-1
for i in range(1,4):
    rear+=1
    lis[rear]=i
for i in range(1,4):
    front+=1
    print(lis[front])
    lis[front]=0
print(front)
print(rear)