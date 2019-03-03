import sys
sys.stdin=open('input.txt','r')

def my_max(x):
    result=-1
    for i in x:
        if result<i:
            result=i
    return result

for tc in range(10):
    _=int(input())
    mat=[list(map(int,input().split())) for i in range(100)]
    resultx=[0]*100
    resulty=[0]*100
    w=0
    z=0
    for i in range(100):
        x=0
        y=0
        for j in range(100):
            x+=mat[i][j]
            y+=mat[j][i]
            if i==j:
                w+=mat[i][j]
            if i+j==99:
                z+=mat[i][j]
        resultx[i]=x
        resulty[i]=y
    x=my_max(resultx)
    y=my_max(resulty)
    result=[x,y,w,z]
    print(f'#{tc+1} {my_max(result)}')