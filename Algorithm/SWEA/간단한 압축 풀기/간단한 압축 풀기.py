import sys
sys.stdin=open('input.txt','r')

testcases=int(input())
for tc in range(testcases):
    print('#{}'.format(tc+1))
    N=int(input())
    lis=[]
    cnt=0
    for _ in range(N):
        lis+=[list(map(str,input().split()))]
    for _ in lis:
        for __ in range(int(_[1])):
            cnt+=1
            print(_[0],end='')
            if cnt==10:
                print()
                cnt=0
    print()