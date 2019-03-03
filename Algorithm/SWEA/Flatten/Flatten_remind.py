import sys
sys.stdin=open('input.txt','r')

def my_max(x):
    result=-1
    for i in x:
        if result<i:
            result=i
    return result

def my_min(x):
    result=999
    for k in x:
        if result>k:
            result=k
    return result


for tc in range(10):
    dump=int(input())
    lis=list(map(int,input().split()))
    cnt=0
    while cnt!=dump:
        for _ in range(len(lis)):
            min=my_min(lis)
            if lis[_]==min:
                lis[_]+=1
                break
        for _ in range(len(lis)):
            max=my_max(lis)
            if lis[_]==max:
                lis[_]-=1
                break
        cnt+=1
    print(f'#{tc+1} {my_max(lis)-my_min(lis)}')