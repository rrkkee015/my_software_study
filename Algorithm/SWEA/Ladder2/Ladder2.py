import sys
sys.stdin=open('input.txt','r')

for _ in range(10):
    tc=int(input())
    mat=[list(map(int,input().split())) for i in range(100)]
    temp_result = 1000
    for init in range(100):
        x=init
        if mat[0][x]==1:
            i=0
            cnt=0
            while i != 99:
                i+=1
                cnt+=1
                if x+1<100 and mat[i][x+1]==1: #오른쪽
                    while x+1<100 and mat[i][x+1]==1:
                        x+=1
                        cnt+=1
                elif 0<=x-1 and mat[i][x-1]==1: #왼쪽
                    while 0<=x-1 and mat[i][x-1]==1:
                        x-=1
                        cnt+=1
            if temp_result>cnt:
                temp_result=cnt
                result=init
    print('#{} {}'.format(tc,result))