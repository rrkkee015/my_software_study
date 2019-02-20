import sys
sys.stdin=open('input.txt','r')

te=10

for t in range(te):
    n=int(input())
    m=[list(map(int,input().split())) for j in range(100)]
    c=0
    for i in range(len(m)):
        T = False
        for k in range(len(m)):
            if matrix[k][i]==1:
                T=True
                continue
            elif m[k][i]==2 and T:
                c+=1
                T=False
    print(f'#{t} {c}')