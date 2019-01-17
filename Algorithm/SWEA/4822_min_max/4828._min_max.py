import sys
sys.stdin=open('sample_input.txt','r')

testcase=int(input())

def my_max(li):
    result = 0
    for max_ in li:
        if result <max_:
            result =max_
    return result

def my_min(li):
    result=li[0]
    for min_ in li:
        if result>min_:
            result=min_
    return result

for k in range(testcase):
    N=int(input())
    ai=list(map(int,input().split()))
    print(f'#{k+1} {my_max(ai)-my_min(ai)}')
        
