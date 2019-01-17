import sys
sys.stdin=open('input.txt','r')

testcase=10

def my_max(li):
    result=0
    for i in li:
        if result<i:
            result=i
    return result

def my_min(li):
    result =li[0]
    for i in li:
        if result>i:
            result=i
    return result
        
for test in range(testcase):
    n=int(input())
    li=list(map(int,input().split()))
    N=0
    while N!=n:
        N+=1
        li[li.index(my_max(li))]=my_max(li)-1
        li[li.index(my_min(li))]=my_min(li)+1
    print(f'#{test+1} {my_max(li)-my_min(li)}')
