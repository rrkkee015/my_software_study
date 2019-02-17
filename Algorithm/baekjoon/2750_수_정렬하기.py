testcases=int(input())
lis=[int(input()) for tc in range(testcases)]
for i in range(len(lis)-1,-1,-1):
    for j in range(0,i):
        if lis[i]<lis[j]:
            lis[i],lis[j]=lis[j],lis[i]
for i in lis:
    print(i)