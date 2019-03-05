N=int(input())
c=0
nc=0
for _ in range(N):
    vo=int(input())
    if vo==1:
        c+=1
    else:
        nc+=1
if c>nc:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")