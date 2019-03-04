def search(x,y):
    if x-y<0:
        return 'done'
    else:
        temp.append(x-y)
        search(temp[-2],temp[-1])

N=int(input())
result=[0,0]
for i in range(N//2,N+1):
    temp=[N,i]
    search(temp[-2], temp[-1])
    cnt=len(temp)
    if result[0]<cnt:
        result[0]=cnt
        result[1]=temp
print(result[0])
for i in result[1]:
    print(i, end=' ')