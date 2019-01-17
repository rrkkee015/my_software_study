import sys
sys.stdin=open('input.txt','r')

for i in range(10):
    t=int(input())
    li=list(map(int,input().split()))
    for i in range(t):
        if 0<max(li)-min(li)<2:
            print(max(li)-min(li))
        else:
            li[li.index(max(li))]-=1
            li[li.index(min(li))]+=1
    print(f'#{i+1} {max(li)-min(li)}')
