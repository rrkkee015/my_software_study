import sys
sys.stdin=open('sample_input.txt','r')

t=int(input())
for i in range(t):
    n,m=tuple(map(int,input().split()))
    li=list(map(int,input().split()))
    result = []
    for a in range(0,n-m+1):
        result.append(sum(li[a:a+m]))
    print(f'#{i+1} {max(result)-min(result)}')
