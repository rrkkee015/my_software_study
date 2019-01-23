import sys
sys.stdin = open('input.txt','r')
testcases=10

for testcase in range(testcases):
    li=[0]*100
    t = int(input())
    for i in range(100):
        li2 = list(map(int, input().split()))
        li[i]=li2
    result=0
    re=0
    re2=0
    for i in range(len(li)):
        for j in range(len(li[i])):
            re+=li[i][j]
        if result<re:
            result=re
        re=0
    for j in range(len(li[0])):
        for i in range(len(li)):
            re+=li[i][j]
        if result<re:
            result=re
        re=0
    for i in range(len(li)):
        for k in range(len(li[i])):
            if i==k:
                re+=li[i][k]
            if i+j==(len(li)-1):
                re2+=li[i][k]
    if result<re:
        result=re
    if result<re2:
        result=re2
    print(f'#{testcase+1} {result}')