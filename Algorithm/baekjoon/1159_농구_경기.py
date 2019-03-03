N=int(input())
temp={}
result=[]
for i in range(N):
    name=input()
    if name[0] not in temp:
        temp[name[0]]=1
    else:
        temp[name[0]]+=1
for k,v in temp.items():
    if v>=5:
        result+=[k]
result.sort()
for k in result:
    print(k,end='')
if result==[]:
    print("PREDAJA")