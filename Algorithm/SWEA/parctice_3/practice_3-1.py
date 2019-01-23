li=[[9,20,2,18,11],[19,1,25,3,21],[8,24,10,17,7],[15,4,16,5,6],[12,13,22,23,14]]
result=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
def my_sort(li):
    nums=li[0][0]
    lis=[]
    for a in range(25):
        for i in range(len(li)):
            for j in range(len(li[i])):
                if nums>li[i][j]:
                    nums=li[i][j]
                    a=i
                    b=j
        lis.append(nums)
        nums=1000
        li[a][b]=9999
    return lis

li=my_sort(li)
li=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
x,y=(2,2)
n=1
a,b=(n,n)
q=1
result[x][y]=li[-1]
for i in li[::-1][1:]: #24 ~ 1까지 순회
    if a!=0:
        y-=1*q
        result[x][y]=i
        a-=1
        continue
    elif b!=0:
        x+=1*q
        result[x][y]=i
        b-=1
    else:
        # q*=-1
        # n+=1
        # a,b=(n,n) #내가 짠
        q*=-1
        y -= 1*q
        result[x][y]=i
        n+=1
        a,b=(n,n)
        a -= 1 # 형이 도와준
print(result)