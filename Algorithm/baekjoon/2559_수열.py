N,K=list(map(int,input().split()))
temp=list(map(int,input().split()))
tem=sum(temp[:K])
result=tem
for i in range(0,N-K):
    tem-=temp[i]
    tem+=temp[K+i]
    if result<tem:
        result=tem
print(result)