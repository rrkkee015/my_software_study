DAY=int(input())
CARS=list(map(int,input().split()))
cnt=0
for i in CARS:
    if i==DAY:
        cnt+=1
print(cnt)