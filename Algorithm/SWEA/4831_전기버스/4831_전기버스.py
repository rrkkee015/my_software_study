import sys
sys.stdin = open('sample_input.txt','r')
t=int(input())
for i in range(t):
    k,n,m=tuple(map(int,input().split()))
    li=list(map(int,input().split()))
    count=0
    end=0
    for c in range(0, m):
        end += k
        if end>=n:
            break
        elif li[c]-li[c-1] > k or li[0] > k or n-li[-1] >k:
            count=0
            break
        for z in li[::-1]:
            if end>=z:
                end=z
                count+=1
                break
    print(f'#{1+i} {count}')
