N=int(input())
result=[]
cnt=0
for i in range(N):
    a,b,c,d=input().split()
    result+=[(int(b),int(c),int(d),a)]

for i in range(len(result)-1,0,-1):
    for j in range(i):
        if result[j][0]<result[j+1][0]:
            result[j],result[j+1]=result[j+1],result[j]

min=0

for i in range(len(result)-1):
    if result[i][0] != result[i+1][0]:
        for i in range(i,min+1,-1):
            for j in range(min+1,i):
                if result[j][1]>result[j+1][1]:
                    result[j],result[j+1]=result[j+1],result[j]
        min=i+1
    if result[i][0]==result[-1][0]:
        for k in range(len(result)-1,min+1,-1):
            for j in range(min,k):
                if result[j][1]>result[j+1][1]:
                    result[j],result[j+1]=result[j+1],result[j]

min =0

for i in range(len(result)-1):
    if result[i][0]==result[i+1][0] and result[i][1]!=result[i+1][1]:
        for k in range(i,min+1,-1):
            for j in range(min+1,k):
                if result[j][2]<result[j+1][2]:
                    result[j],result[j+1]=result[j+1],result[j]
        min=i+1
    if result[i][0]==result[-1][0] and result[i][1] == result[-1][1]:
        for p in range(len(result)-1,min+1,-1):
            for j in range(min,p):
                if result[j][2]>result[j+1][2]:
                    result[j],result[j+1]=result[j+1],result[j]

for i in result:
    print(i)
