R,C=list(map(int,input().split()))
hill=[[0]*C for i in range(R)]
result=1
BP=False
for _ in range(R):
    inp=input()
    for i in range(len(inp)):
        hill[_][i]=inp[i]
dxdy=[(0,1),(1,0),(-1,0),(0,-1)]
for i in range(R):
    for j in range(C):
        if hill[i][j]=='.':
            hill[i][j]='D'
        elif hill[i][j]=='S':
            for _ in dxdy:
                if 0<=i+_[0]<R and 0<=j+_[1]<C and hill[i+_[0]][j+_[1]]=='W':
                    result=0
                    BP=True
                    break
        if BP:
            break
    if BP:
        break
if BP:
    print(result)
else:
    print(result)
    for i in range(R):
        result=''
        for j in range(C):
            result+=str(hill[i][j])
        print(result)