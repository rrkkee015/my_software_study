import sys
sys.stdin=open('sample_input.txt','r')

def winner(end,P):
    st=1
    cnt=0
    while True:
        mid = int((end+st)/2)
        if P == mid:
            cnt+=1
            break
        elif mid < P:
            st=mid
            cnt+=1
        elif P < mid:
            end=mid
            cnt+=1
    return cnt

def who(a,b):
    if a==b:
        return 0
    elif a>b:
        return 'B'
    else:
        return 'A'

testcases=int(input())
for test in range(testcases):
    end,Pa,Pb=tuple(map(int,input().split()))
    A=winner(end,Pa)
    B=winner(end,Pb)
    print(f'#{test+1} {who(A,B)}')
