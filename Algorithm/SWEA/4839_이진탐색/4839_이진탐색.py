import sys
sys.stdin = open('sample_input.txt','r')
testcases = int(input())
for test in range(testcases):
    end,Pa,Pb = tuple(map(int,input().split()))
    st=1

    def page(st, end, fin):
        cnt = 0
        while True:
            center=int((st+end)/2)
            cnt+=1
            if center == fin:
                break
            else:
                if center < fin:
                    st=center
                else:
                    end=center
        return cnt

    def winner(A,B):
        if A==B:
            result=0
        elif A>B:
            result='B'
        else:
            result='A'
        return result

    A=page(st,end,Pa)
    B=page(st,end,Pb)

    result=winner(A,B)

    print(f'#{test+1} {result}')



