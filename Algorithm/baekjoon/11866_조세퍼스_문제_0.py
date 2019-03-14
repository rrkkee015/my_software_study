from collections import deque

N,M=list(map(int,input().split()))
lis=[]
for _ in range(1,N+1):
    lis+=[_]
jo=deque(lis)
print('<',end='')
while jo:
    if len(jo) == 1:
        temp=jo.popleft()
        print(temp, end='')
    else:
        jo.rotate(-M+1)
        temp=jo.popleft()
        print(temp, end=', ')
print('>')