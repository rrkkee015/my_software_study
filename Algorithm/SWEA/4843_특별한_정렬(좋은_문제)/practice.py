import sys
sys.stdin = open('sample_input.txt','r')
testcases=int(input())
for test in range(testcases):
    i=0
    n=int(input())
    li=list(map(int,input().split()))
    for tt in range(5):
        maxIndex = 2 * i
        minIndex = 2 * i + 1

        if li[maxIndex]<li[minIndex]:
            li[maxIndex],li[minIndex]=li[minIndex],li[maxIndex]

        for k in range(2*i+2,len(li)):
            if li[maxIndex]<li[k]:
                maxIndex=k
        li[2*i],li[maxIndex]=li[maxIndex],li[2*i]

        for a in range(2*i+2,len(li)):
            if li[minIndex]>li[a]:
                minIndex=a
        li[2*i+1],li[minIndex]=li[minIndex],li[2*i+1]

        i+=1
    result= ' '.join(list(map(str,li[:10])))

    print(f'#{test+1} {result}')