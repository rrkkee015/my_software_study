N,K=list(map(int,input().split()))
lis=list(map(int,input().split()))
s=sum(lis[:K])
result=s
for _ in range(1,N-K+1):
    if s>result:
        result=s
    s=s-lis[_-1]+lis[K+_-1]
if s>result:
    result=s
print(result)


# N,K=list(map(int,input().split()))
# temp=list(map(int,input().split()))
# tem=sum(temp[:K])
# result=tem
# for i in range(0,N-K):
#     tem-=temp[i]
#     tem+=temp[K+i]
#     if result<tem:
#         result=tem
# print(result)