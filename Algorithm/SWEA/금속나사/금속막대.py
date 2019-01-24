import sys
sys.stdin=open('input.txt','r')
testcases=int(input())
for test in range(testcases):
    n=int(input())
    real_result=''
    li = list(map(int,input().split()))
    result=[0]*n
    i=0
    for k in range(len(result)):
        result[k] = [li[i],li[i+1]]
        i+=2
    ##################

    ##################
    for i in result:
        x=0
        nasa = [0] * n
        nasa[x]=i
        cnt=1
        for k in result:
            if i == k:
                continue
            if nasa[x][1] in dic.keys():
                x += 1
                nasa[x]=result[dic[nasa[x-1][1]]]
                cnt+=1
        if cnt == len(result):
            break
    for k in range(len(nasa)):
        for i in range(len(nasa[k])):
            real_result += str(nasa[k][i])+ ' '
    print(f'#{test+1} {real_result}')