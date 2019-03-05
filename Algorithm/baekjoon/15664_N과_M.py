N,M=list(map(int,input().split()))
lis=list(map(int,input().split()))
result=[]
for i in range(1<<N):
    temp=[]
    for j in range(N):
        if i & 1<<j:
            temp+=[lis[j]]
    if len(temp)==M and sorted(temp) not in result:
        result+=[sorted(temp)]
for _ in sorted(result):
    for i in _:
        print(i, end=' ')
    print()
































# N,M=list(map(int,input().split()))
# l=list(map(int,input().split()))
# r=[]
# for i in range(1<<len(l)):
#     t=[]
#     for j in range(len(l)):
#         if i & 1<<j:t+=[l[j]]
#     if len(t)==M and sorted(t) not in r:r+=[sorted(t)]
# r=sorted(r)
# for i in r:
#     for k in i:
#         print(k, end=' ')
#     print()