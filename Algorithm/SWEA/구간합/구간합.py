import sys
sys.stdin=open('sample_input.txt','r')

def my_sum(li):
    result = 0
    for i in li:
        result += i
    return result

def M_sum(li,M):
    result=[]
    for i in range(len(li)-M+1):
        result.append(my_sum(li[i:i+M]))
    return result

def my_max(li):
    result=0
    for i in li:
        if result<i:
            result=i
    return result

def my_min(li):
    result = li[0]
    for i in li:
        if result>i:
            result=i
    return result

def result(li):
    return my_max(li)-my_min(li)

testcase=int(input())

for test in range(testcase):
    N,M=tuple(map(int,input().split()))
    ai=list(map(int,input().split()))
    li=M_sum(ai,M)
    print(result(li))
