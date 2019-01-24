import sys
sys.stdin=open('sample_input.txt','r')
testcases=int(input())

for test in range(testcases):
    li = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(10)]
    def red(a,b,c,d):
        a,b=a,b
        c,d=c,d
        for i in range(0,b-a+1):
            for j in range(0, d-c+1):
                li[a+i][c+j]+=1
        return li

    def blue(a,b,c,d):
        a, b = a,b
        c, d = c,d
        for i in range(0, b - a + 1):
            for j in range(0, d - c + 1):
                li[a + i][c + j]+= 2
        return li

    def purple(li):
        cnt=0
        for i in range(len(li)):
            for j in range(len(li[i])):
                if li[i][j] == 3:
                    cnt+=1
        return cnt

    subtests=int(input())

    for sub in range(subtests):
        a,c,b,d,z=tuple(map(int,input().split()))
        if z == 1:
            li=red(a,b,c,d)
        else:
            li=blue(a,b,c,d)
    cnt=purple(li)
    print(f'#{test+1} {cnt}')